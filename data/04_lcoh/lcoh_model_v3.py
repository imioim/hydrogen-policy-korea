# -*- coding: utf-8 -*-
"""
울산·삼척 해상풍력 연계 수전해 LCOH 모형 v3
변경점(v2→v3)
- 통화: 모든 계산·출력 USD. 원화 입력값은 1,470원/USD 한 값으로 환산(환율 민감도 제거).
- 시계열: Weibull 합성 → Renewables.ninja(MERRA-2, 2019) 실측 재분석 시계열.
  풍력: Vestas V164 8MW 곡선, 80m 허브. 수준은 GWA 150m 기준 순이용률(울산 0.42, 삼척 0.33)에
  거듭제곱 변환 cf' = cf^a 로 맞춤(0과 1은 고정, 시간 분포 유지).
  태양광: 35° 고정, 시스템 손실 10%, 원자료 그대로(울산 0.176, 삼척 0.181).
- 운전 방식: direct(직결, 잉여 폐기) / hybrid(잉여 판매) / ppa(계통 경유 PPA, 망이용료 가산) /
  curtail(제약전력 흡수) / wind+solar(하이브리드 직결 또는 잉여 판매)
"""
import numpy as np, pandas as pd, math, sys, os
HERE=os.path.dirname(os.path.abspath(__file__))
FX=1470.0   # 원/USD. 원화 입력값 환산 전용(2026년 보도 범위 1,468~1,481원; 한국은행 월평균으로 확정 필요)
def won(x_won_per_kwh): return x_won_per_kwh/FX*1000   # 원/kWh → USD/MWh
def wonkg(x): return x/FX                                # 원/kg → USD/kg

I=dict(
    years=20, r=0.07,
    kwh_per_kg=55.0, stack_life_h=70000, stack_cost_frac=0.20, opex_frac=0.03,
    water_usd_per_kg=wonkg(30), min_load=0.10,
    capex_usd_per_kw={'2026':2200,'2030':1700,'2035':1000,'2035 낙관':800},   # IEA GHR 2026 비중국산 기준, 2035 추세 가정
    lcoe_usd_per_mwh={'울산':{'2026':won(175),'2030':won(150),'2035':won(115)}},   # 부유식 상한 175.1원(2026 입찰) 기준
    grid_sell_usd_per_mwh=won(130),       # 잉여 판매(SMP 연평균 가정 130원)
    grid_fee_usd_per_mwh=won(12),         # PPA 망이용료 가정
    curtail_usd_per_mwh=won(30),          # 제약전력 인수 단가 가정
    storage_usd_per_kg={'압축 현지':wonkg(400),'액화':wonkg(2800),'암모니아 반출':wonkg(1200)},
    target_cf={'울산':0.42,'삼척':0.33},  # GWA 150m, 손실 17% 반영 순이용률
    bench={'수입 분해수소 2030NZE':5.69,'수입 분해수소 2030중앙':7.23,'수입 분해수소 2023':8.92,
           '수입 암모니아 2030NZE':3.79,'수입 암모니아 2030중앙':4.92,'수입 암모니아 2023':6.17},
)
# 삼척 풍력 LCOE: 동일 설비비, 이용률 비 환산
I['lcoe_usd_per_mwh']['삼척']={y:v*0.42/0.33 for y,v in I['lcoe_usd_per_mwh']['울산'].items()}

def load(name):
    df=pd.read_csv(os.path.join(HERE,name),comment='#'); return df['electricity'].to_numpy(float)
def fit_power(cf,target):
    lo,hi=0.2,5.0
    for _ in range(60):
        a=(lo+hi)/2
        if (cf**a).mean()>target: lo=a
        else: hi=a
    return a, cf**a
WIND={}; SOLAR={}; META={}
for s,f in [('울산','wind_ulsan_2019.csv'),('삼척','wind_samcheok_2019.csv')]:
    raw=load(f); a,adj=fit_power(raw,I['target_cf'][s]); WIND[s]=adj
    META[s]=dict(raw_cf=raw.mean(),alpha=a,adj_cf=adj.mean(),zero_h=int((raw==0).sum()),full_h=int((adj>0.9).sum()))
for s,f in [('울산','solar_ulsan_2019.csv'),('삼척','solar_samcheok_2019.csv')]:
    SOLAR[s]=load(f)

def crf(r,n): return r*(1+r)**n/((1+r)**n-1)

def lcoh(gen, mode, capex, lcoe, ratio, storage='압축 현지', site=None, g=None, extra_elec_mwh=0.0):
    """gen: 발전 출력(정격 1kW 기준, 8760). ratio: 수전해 kW / 발전 kW.
    direct: 잉여 폐기. hybrid: 잉여 판매. ppa: 계통 경유, 수전해가 gen 전량을 받되 CF는 ratio로 제한 없음(ratio=1).
    curtail: 송전한도 g 초과분만 수전해(가격 curtail)."""
    cap=ratio
    if mode in ('direct','hybrid'):
        use=np.minimum(gen,cap); use=np.where(use<cap*I['min_load'],0,use); surplus=gen-use
        price=lcoe
    elif mode=='ppa':
        use=np.minimum(gen,cap); use=np.where(use<cap*I['min_load'],0,use); surplus=gen-use
        price=lcoe+I['grid_fee_usd_per_mwh']
    elif mode=='curtail':
        use=np.clip(gen-g,0,cap); use=np.where(use<cap*I['min_load'],0,use); surplus=np.zeros_like(gen)
        price=I['curtail_usd_per_mwh']
    E=use.sum()                      # kWh per kW_gen-year
    H2=E/I['kwh_per_kg']; cf_elz=E/(cap*8760)
    capex_tot=capex*cap
    ann=capex_tot*crf(I['r'],I['years'])
    stack=capex_tot*I['stack_cost_frac']*(cf_elz*8760/I['stack_life_h'])
    opex=capex_tot*I['opex_frac']
    elec=E/1000*price
    rev=surplus.sum()/1000*I['grid_sell_usd_per_mwh'] if mode=='hybrid' else 0.0
    c=(ann+stack+opex+elec-rev)/H2 + I['water_usd_per_kg'] + I['storage_usd_per_kg'][storage]
    return dict(lcoh=c, cf_elz=cf_elz, kg_per_kw=H2, elec_share=(elec-rev)/H2/c if c>0 else np.nan)

def hybrid_ws(site, year, capex, solar_ratio, elz_ratio, sell=False):
    """풍력 1kW + 태양광 solar_ratio kW → 수전해 elz_ratio kW. 전력 단가는 풍력 LCOE와 태양광 LCOE 가중."""
    solar_lcoe=won({'2026':120,'2030':105,'2035':90}[year])   # 태양광 단가 가정(2026 입찰 상한 범위, 출처 보완 필요)
    gen=WIND[site]+solar_ratio*SOLAR[site]
    w_e=WIND[site].sum(); s_e=solar_ratio*SOLAR[site].sum()
    lcoe=(w_e*I['lcoe_usd_per_mwh'][site][year]+s_e*solar_lcoe)/(w_e+s_e)
    return lcoh(gen,'hybrid' if sell else 'direct',capex,lcoe,elz_ratio)

if __name__=='__main__':
    rows=[]
    for s in ['울산','삼척']:
        m=META[s]; print(f"{s}: ninja 원 CF {m['raw_cf']:.3f} → 보정 지수 a={m['alpha']:.3f}, 보정 CF {m['adj_cf']:.3f}, 정지 {m['zero_h']}h, 태양광 CF {SOLAR[s].mean():.3f}")
        for y,capex in I['capex_usd_per_kw'].items():
            yr=y.split()[0]; lcoe=I['lcoe_usd_per_mwh'][s][yr]
            for mode in ['direct','hybrid','ppa']:
                for ratio in ([0.5,0.7,1.0] if mode!='ppa' else [1.0]):
                    for st in I['storage_usd_per_kg']:
                        r=lcoh(WIND[s],mode,capex,lcoe,ratio,st)
                        rows.append(dict(site=s,capex_case=y,capex=capex,lcoe=round(lcoe,1),mode=mode,ratio=ratio,storage=st,**{k:round(v,3) for k,v in r.items()}))
    df=pd.DataFrame(rows); df.to_csv(os.path.join(HERE,'lcoh_results_v3.csv'),index=False,encoding='utf-8-sig')
    print('\n== 2035 설비비 1,000 $/kW, 압축 현지 ==')
    q=df[(df.capex_case=='2035')&(df.storage=='압축 현지')]
    print(q.pivot_table(index=['mode','ratio'],columns='site',values='lcoh').round(2))
    print('\n== 제약전력 흡수형(삼척 2035, 1,000 $/kW, 20.4 $/MWh) ==')
    for g in [0.3,0.5,0.7]:
        for ratio in [0.3,0.5]:
            r=lcoh(WIND['삼척'],'curtail',1000,None,ratio,g=g); print(f"  g={g} ratio={ratio}: LCOH {r['lcoh']:.2f} CF {r['cf_elz']:.2f}")
    print('\n== 풍력+태양광 하이브리드 2035 1,000 $/kW ==')
    for s in ['울산','삼척']:
        for sr in [0.5,1.0,1.5]:
            for sell in [False,True]:
                r=hybrid_ws(s,'2035',1000,sr,1.0,sell); print(f"  {s} 태양광 {sr}배 {'판매' if sell else '직결'}: LCOH {r['lcoh']:.2f} CF {r['cf_elz']:.2f}")
