# hydrogen-policy-korea — 데이터와 코드 / Data and code

논문: '생산지 중심 수소 경제' 명제로 본 한국 그린수소 정책의 공백과 재설계 — 유럽 해상풍력 연계 수전해 사례의 입지 조건 분석 (울산·동해삼척 클러스터)
Paper: Gaps and redesign of Korea's green hydrogen policy under the 'production-site-centred hydrogen economy' proposition — site conditions of European offshore-wind-linked electrolysis cases, applied to the Ulsan and Donghae–Samcheok clusters.

저자 / Author: 임정혁 (Im Jeong-hyuk), Ajou University.  
기준일 / As of: 2026-11-16. 분석 기준일 / Analysis date: 2026-11-16 (coding v4), 2026-11-08 (site recalculation).

학술 논문 PDF는 저작권에 따라 포함하지 않았다. IEA 데이터베이스 원본은 CC BY 4.0으로 공개되어 있어 포함했다.  
Journal article PDFs are not included (copyright). The IEA database files are included under their CC BY 4.0 licence.

## 폴더 구성 / Structure

이 파일은 저장소 `data/` 폴더의 설명이다. 그림 파일(PNG)은 저장소 `figures/` 폴더에 있다. / This file documents the repository's `data/` folder; image files are in `figures/`.

### data/01_cases — 유럽 사례 fsQCA / European cases, fsQCA

현재 분석은 v4(2026-11-16)다. v2·v3 파일은 이력으로 남긴다. / Current analysis is v4; v2–v3 files are kept as history.

| 파일 | 내용 | 출처·비고 |
|---|---|---|
| IEA_Hydrogen_Production_Projects_Database_2026-06.xlsx, IEA_Hydrogen_Infrastructure_Projects_Database_2026-06.xlsx | IEA Hydrogen Production and Infrastructure Projects Database, 2026년 6월판 원본. 모집단 추출의 출처 | IEA, CC BY 4.0. https://www.iea.org/data-and-statistics/data-product/hydrogen-production-and-infrastructure-projects-database |
| european_cases_coding_v4.xlsx | 47건 코딩표 v4(시트: 코딩표, 코딩 지침, fsQCA 설계, fsQCA 소속값). 본 분석 40건. 제외 7건: 실체·전력원 미확인 3건(8 HEAL, 14 Lowestoft, 28 Mukran), 해상풍력 연계가 아닌 4건(2 Brande 육상풍력 직결, 3 OceanH2 실험실 규모, 6 Deep Purple 육상 파일럿, 7 HyPilot 계통 전력 시험). 재코딩: 15 SUPPORT 1(IPCEI Waterstof), 18·19 SUPPORT 0.55(니더작센주 보조금)·LOCAL 1(같은 부지 사용), 9 OFFTAKE 0.33(구속력 있는 공급계약 미확인), 24·36 SMALL 0.67(발표 규모 100MW). 21은 덴마크 PtX 입찰 선정 확인으로 0.55 유지, 5는 중단 근거 없어 0.6 유지 | IEA DB에서 발췌한 필드 + 저자 코딩. 근거 URL과 확인일은 '코딩 비고' 열 |
| fsqca_input_v4.csv | R 입력(40+7건, 7조건·결과 소속값, 제외 표시·사유) | 저자 |
| fsqca_run_v4.R | QCA 패키지 실행 스크립트(R 4.3.3, QCA 3.25.8). 본 분석 40건, 강건성 47건 | 저자 |
| result_v4.txt | 실행 결과 원문 | 저자 실행 |
| fsqca_result_tables_v4.xlsx | 보정표·진리표·해 요약·필요조건·강건성 | 저자 |
| european_cases_coding_final.xlsx | v3 코딩표(본 분석 44건, 제외 후보 3건). 2026-11-09 수정: DEMO 8건 성립 소속값 0.8→0.6, 27·35번 비고 보완 | 이력 |
| fsqca_input_v2.csv, fsqca_run_v3.R, result_v3.txt, fsqca_result_tables_v3.xlsx | v3 분석(44건) 입력·스크립트·결과·결과표 | 이력 |

### data/02_legal — 법령 대조 / Legal comparison
| 파일 | 내용 | 출처·비고 |
|---|---|---|
| legal_comparison_v1.xlsx | EU(RED II 27(3), 2023/1184, 2023/1185, RED III) 대 한국(수소법·시행령·인증 고시·해상풍력법·분산에너지법·전기사업법) 조항별 네 기준 판정 | 2026-11-08 확인 사항: 2023/1185 행은 '산정 방법·비교값 94 gCO2eq/MJ'(70% 기준은 RED II Art.25(2)); RED III 조문 Art.22a·25; 직접 PPA 근거 전기사업법 제2조·제7조의2·제16조의5. 11차 전력수급기본계획 행: 2026-11-16 확인 — 수전해 수소 생산의 전력 수요는 수요 전망(EGMS)에 반영, 수전해 설비의 위치·접속은 미반영; 장기 송변전설비계획(2024~2038)에 수전해 없음 |

### data/03_site — 입지 / Site conditions
| 파일 | 내용 | 출처·비고 |
|---|---|---|
| site_assessment_oct2026.xlsx | 10월 판정표(순위표, 가중치 민감도, 연계 조건표 12항목) | 저자. 11월 재계산으로 일부 수치 대체(아래 v2 파일 참조) |
| site_ranking_v2.xlsx | 수정 순위표(울산 88.0 / 삼척 남부 대륙붕 62.0 / 삼척 남부 외측 59.0 / 동해시·삼척 북부 47.0)와 18개 가중치 시나리오 | 저자, 2026-11-08 |
| bathymetry_zoning_v2.xlsx | 네 후보 해역의 수심 분포·해안 거리·영해 안 비율·용도구역 중첩, 60m 이하 띠 분석 | BADA2024 + 해양공간관리계획 고시 공간정보, 저자 계산 |
| zoning_overlap_v1.xlsx | 직사각형 경계 기준 1차 용도구역 중첩(참고) | 저자 |
| wind_resource_cf.xlsx | GWA 3.0 150m 풍속·와이블 모수 집계, IEA 15MW 곡선 총이용률, 손실 17% 가정 순이용률 | Global Wind Atlas 3.0 (DTU/World Bank) 격자에서 저자 집계. GWA 격자 원본 미포함(https://globalwindatlas.info) |
| grid_connection_points.xlsx | 양륙 후보·직선거리·한전ON 연계가능 용량(2026-10-25 조회) | 저자 정리 |
| bada/bada_ulsan.txt, bada/bada_yeongdong.txt | BADA2024 수심 격자 추출(경도·위도·수심) | 국립해양조사원 해양수치모델 전용 수심 BADA2024(150m 격자, 2025.2 공개). 공공데이터 |
| msp_zones/msp_ulsan_zones.zip, msp_gangwon_zones.zip | 해양공간관리계획 고시 공간정보(PRPOS_0100~0900: 어업활동보호/골재·광물/에너지개발/해양관광/환경·생태계관리/연구·교육보전/항만·항행/군사활동/안전관리), WGS84 | 해양공간통합관리정보시스템(msp.go.kr). 울산광역시 계획 2022.5.30 고시, 강원특별자치도 계획 2022.4.25 고시. 공공데이터 |
| ../figures/wind150m_bathymetry_ulsan_yeongdong.png | GWA 150m 풍속과 BADA 60·200m 등수심선 지도 | 저자 작성 |
| ../figures/kigam_*.png | 지오빅데이터 오픈플랫폼 해저지질정보 화면(1:25만 해저지질도 인덱스, 퇴적물 유형분포도 동해, 제20집 강릉–삼척해역 2009, 제21집 울산해역 2011) | 한국지질자원연구원 포털 화면 캡처, 참고용 |

후보 해역 정의(bathymetry_zoning_v2.xlsx '방법' 시트): 울산 부유식 해역 35.30~35.60N·해안 50~72km; 삼척 남부 대륙붕 37.20~37.35N·10~20km; 삼척 남부 외측 37.20~37.35N·20~30km; 동해시·삼척 북부 37.40~37.60N·3~15km. 해안선은 BADA 수심 3m 이하 격자점으로 대신함.

### data/04_lcoh — 수소 단가 / LCOH
| 파일 | 내용 | 출처·비고 |
|---|---|---|
| lcoh_model_v4.py | LCOH 모형 v4(USD, 환율 1,470원/USD, 운전 5방식, cf^a 보정). 풍력 발전단가 두 경로(A 입찰가: 2026년 175원/kWh 상한가에서 150·115원; B 비용: 195·165·135원), 비교행 C(안지영·김기환 2024의 전력 가정 290.58원/kWh·가동률 0.90), 수입 비교 기준 2030년 두 열과 국내 연구 기준값 5.65 USD/kg. 순이용률 입력 울산 0.43·삼척 0.34(wind_resource_cf.xlsx의 0.4316·0.3386). 태양광 발전단가는 2026년 제1차 태양광 고정가격계약 경쟁입찰 공고(신·재생에너지센터 공고 제2026-23호, 2026.7.16.)의 육지 상한가 147,686원/MWh, 2030·2035년은 풍력 경로 A와 같은 비율로 하락 가정(126.5·97.0원/kWh) | 저자, 2026-11-17 |
| lcoh_results_v4.csv | 336개 조합(경로 2 × 지역 2 × 설비비 4 × 운전·용량비 7 × 저장 3) 결과 | 저자 |
| lcoh_run_v4.txt | 실행 출력(보정 지수, 표, 비교행 C, 제약전력, 풍력+태양광 하이브리드, 태양광 단독) | 저자 실행 |
| lcoh_solar_only_v4.csv | 태양광 단독 직결 6개 조합(2035년, 울산·삼척 × 용량비 1.0/0.7/0.5) 결과 | 저자 |
| lcoh_model_v3.py, lcoh_results_v3.csv | v3 모형·결과(경로 A만, 순이용률 0.42/0.33). 이력 | 이력 |
| wind_ulsan_2019.csv (35.45N 129.75E), wind_samcheok_2019.csv (37.31N 129.55E), solar_ulsan_2019.csv (35.5N 129.3E), solar_samcheok_2019.csv (37.4N 129.15E) | 2019년 시간별 이용률, MERRA-2, 풍력 V164 8MW 80m, 태양광 35° 손실 10% | Renewables.ninja (Staffell & Pfenninger 2016; Pfenninger & Staffell 2016). **CC BY-NC 4.0** — 비상업 이용·출처 표기 조건 |
| lcoh_measured_series_v3.xlsx | 입력값·월별 시계열·운전방식·제약전력·하이브리드·벤치마크 | 저자 |
| imported_hydrogen_delivered_cost_v1.xlsx | 수입 그린수소 도착 단가(호주 수전해→암모니아→해상 운송→울산 도착→분해). 분해 후 수소 5.69 / 7.23 / 8.92, 암모니아 3.79 / 4.92 / 6.17 USD/kg의 산출 시트(수식 포함). 환율 1,470원 | IEA Global Hydrogen Review 2024 Assumptions Annex의 비용 가정(전해조 2,160→960 USD/kW, 효율 66→69%, O&M 3%, 스택 50,000 h, Haber-Bosch 770 USD/(tNH3/y), 분해 3,050 USD/(tH2/y), 탱커 51,800 t) + 저자 가정(전력 30 USD/MWh, FLH 4,500 h, 터미널 0.10 USD/kg, 분해 전력 0.09 USD/kWh, WACC 7%, 20년). 2030년 두 열(5.69, 7.23)은 적힌 가정으로 재현됨. 2023년 열은 재현되지 않아(해외 생산 LCOH 5.27 대 4.97) 논문의 비교 기준에서 제외. 2030년 중앙 열의 전해조 1,700 USD/kW는 IEA Global Hydrogen Review 2026의 중국 외 2030년 범위(1,500~1,900)의 중간값 |

## 재현 / Reproduction
- fsQCA: `Rscript data/01_cases/fsqca_run_v4.R` (fsqca_input_v4.csv와 같은 폴더에서). 입력 CSV가 UTF-8(BOM)이므로 UTF-8 로캘에서 실행한다. Linux/macOS: `LC_ALL=C.UTF-8 Rscript fsqca_run_v4.R`; Windows PowerShell: 실행 전 `$env:LANG="ko_KR.UTF-8"`. 로캘이 맞지 않으면 R이 25행만 읽고 멈춘다.
- LCOH: `python data/04_lcoh/lcoh_model_v4.py` (ninja CSV 4개와 같은 폴더). numpy, pandas 필요. 결과는 lcoh_results_v4.csv와 lcoh_solar_only_v4.csv로 저장된다.
- 입지: bathymetry_zoning_v2.xlsx '방법' 시트의 절차. geopandas, shapely, scipy 사용.

## 이용 조건 / Licensing
- 저자 작성 파일(코딩표, 스크립트, 결과표, 계산표): CC BY 4.0.
- IEA Hydrogen Production and Infrastructure Projects Database 원본: CC BY 4.0 (IEA 원 라이선스 유지, 출처 표기).
- Renewables.ninja CSV: CC BY-NC 4.0 (원 라이선스 유지).
- BADA2024, 해양공간관리계획 공간정보: 각 기관의 공공데이터 이용 조건에 따름. 출처 표기.
- KIGAM 화면 캡처: 참고용, 원자료는 지오빅데이터 오픈플랫폼(https://data.kigam.re.kr).

## 변경 기록 / Changelog
- 2026-11-17: LCOH v4의 태양광 발전단가를 저자 가정(120·105·90원/kWh)에서 2026년 제1차 태양광 고정가격계약 경쟁입찰 상한가(147.7원/kWh) 기준으로 교체(2030·2035년은 풍력 경로 A와 같은 비율로 하락). 태양광 단독 직결 계산과 lcoh_solar_only_v4.csv 추가. 풍력만 쓰는 구성의 결과(lcoh_results_v4.csv)는 변동 없음.
- 2026-11-16: fsQCA v4. 해상풍력 연계가 아닌 4건(2, 3, 6, 7) 제외로 본 분석 40건. 재코딩 6건(9, 15, 18, 19, 24, 36)을 사업자·정부 원자료로 확인해 반영, 5·21은 확인 뒤 유지. 코딩표·입력·스크립트·결과·결과표 v4 추가, v3 파일은 이력으로 보존. IEA DB 원본 2종 추가(CC BY 4.0). 수입 수소 비교 기준에서 2023년 열 제외(가정으로 재현되지 않음). 법령 대조표의 11차 전력수급기본계획 행 확인 사항 기록. LCOH v4 추가(경로 A·B, 비교행 C)하고 순이용률 입력을 0.42/0.33에서 0.43/0.34로 정정(풍황 시트와 일치). 입지 재계산: 부유식 수심 범위 50~1,000m, 고정식 띠 50m 미만(World Bank Group 2019 기준).
- 2026-11-09: 수입 수소 도착 단가 산출 시트 추가(imported_hydrogen_delivered_cost_v1.xlsx). 코딩표 DEMO 소속값 0.6으로 통일, 27(AquaSector)·35(Dogger Bank) 비고 보완. 입지 v2(BADA·용도구역 재계산, 삼척 남부 외측 수심 점수 0.9→0.7). 비교 기준을 수입 분해수소 하나로 통일.
- 2026-10-26: 코딩표 최종(사유 변경 27→5, 30→2; 휴면 0.3 조정 26·36·37; 제외 8·14·28). LCOH v3(USD, 실측 시계열).
