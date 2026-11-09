# hydrogen-policy-korea — 데이터와 코드 / Data and code

논문: 생산 입지 중심 경제로 본 한국 그린수소 정책의 공백과 재설계 — 유럽 해상풍력 연계 수전해 사례의 입지 조건 분석 (울산·동해삼척 클러스터)
Paper: Gaps and redesign of Korea's green hydrogen policy from a production-site-centered economy — site conditions of European offshore-wind-linked electrolysis cases, applied to the Ulsan and Donghae–Samcheok clusters.

저자 / Author: 임정혁 (Im Jeong-hyuk), Ajou University.  
기준일 / As of: 2026-11-09. 분석 기준일 / Analysis date: 2026-10-26 (coding), 2026-11-08 (site recalculation).

학술 논문 PDF와 IEA 데이터베이스 원본은 저작권·이용약관에 따라 포함하지 않았다. 아래 출처 링크를 참조.  
Journal article PDFs and the original IEA database file are not included (copyright / terms of use). See source links below.

## 폴더 구성 / Structure

이 파일은 저장소 `data/` 폴더의 설명이다. 그림 파일(PNG)은 저장소 `figures/` 폴더에 있다. / This file documents the repository's `data/` folder; image files are in `figures/`.

### data/01_cases — 유럽 사례 fsQCA / European cases, fsQCA
| 파일 | 내용 | 출처·비고 |
|---|---|---|
| european_cases_coding_final.xlsx | 47건 코딩표(시트: 코딩표, 코딩 지침, fsQCA 설계, fsQCA 소속값). 본 분석 44건, 제외 후보 3건(8 HEAL, 14 Lowestoft, 28 Mukran) | IEA Hydrogen Production Projects Database (June 2026)에서 발췌한 필드(사업명·국가·상태·용량·전력 유형·용도·위치) + 저자 코딩. 2026-11-09 수정: DEMO 8건 성립 소속값 0.8→0.6(분석에 쓴 값으로 통일), 27·35번 비고 보완 |
| fsqca_input_v2.csv | R 입력(44+3건, 7조건·결과 소속값) | 저자 |
| fsqca_run_v3.R | QCA 패키지 실행 스크립트(R 4.6.1, QCA 3.25) | 저자 |
| result_v3.txt | 실행 결과 원문 | 저자 실행 |
| fsqca_result_tables_v3.xlsx | 보정표·진리표·해 요약·강건성 | 저자 |

IEA DB: https://www.iea.org/data-and-statistics/data-product/hydrogen-production-and-infrastructure-projects-database (원본 미포함 / original not included).

### data/02_legal — 법령 대조 / Legal comparison
| legal_comparison_v1.xlsx | EU(RED II 27(3), 2023/1184, 2023/1185, RED III) 대 한국(수소법·시행령·인증 고시·해상풍력법·분산에너지법·전기사업법) 조항별 네 기준 판정 | 2026-11-08 확인 사항: 2023/1185 행은 '산정 방법·비교값 94 gCO2eq/MJ'(70% 기준은 RED II Art.25(2)); RED III 조문 Art.22a·25; 직접 PPA 근거 전기사업법 제2조·제7조의2·제16조의5; 11차 전기본 행은 미확인으로 삭제 예정 |

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
| lcoh_model_v3.py | LCOH 모형(USD, 환율 1,470원/USD, 운전 5방식, cf^a 보정) | 저자 |
| wind_ulsan_2019.csv (35.45N 129.75E), wind_samcheok_2019.csv (37.31N 129.55E), solar_ulsan_2019.csv (35.5N 129.3E), solar_samcheok_2019.csv (37.4N 129.15E) | 2019년 시간별 이용률, MERRA-2, 풍력 V164 8MW 80m, 태양광 35° 손실 10% | Renewables.ninja (Staffell & Pfenninger 2016; Pfenninger & Staffell 2016). **CC BY-NC 4.0** — 비상업 이용·출처 표기 조건 |
| lcoh_results_v3.csv | 168개 조합 결과 | 저자 |
| lcoh_measured_series_v3.xlsx | 입력값·월별 시계열·운전방식·제약전력·하이브리드·벤치마크 | 저자 |

| imported_hydrogen_delivered_cost_v1.xlsx | 수입 그린수소 도착 단가(호주 수전해→암모니아→해상 운송→울산 도착→분해). 벤치마크 분해수소 5.69 / 7.23 / 8.92, 암모니아 3.79 / 4.92 / 6.17 USD/kg의 산출 시트(수식 포함). 환율 1,470원 | IEA Global Hydrogen Review 2024 Assumptions Annex의 비용 가정 + 저자 가정(전력 30 $/MWh, FLH 4,500 h, 터미널 0.10 $/kg, 분해 전력 0.09 $/kWh). 2023 열 해외 생산 LCOH 5.27은 적힌 가정으로 4.97이 재현되어 확인 중 |

## 재현 / Reproduction
- fsQCA: `Rscript data/01_cases/fsqca_run_v3.R` (fsqca_input_v2.csv와 같은 폴더에서). 
- LCOH: `python data/04_lcoh/lcoh_model_v3.py` (ninja CSV 4개와 같은 폴더). numpy, pandas 필요.
- 입지: bathymetry_zoning_v2.xlsx '방법' 시트의 절차. geopandas, shapely, scipy 사용.

## 이용 조건 / Licensing
- 저자 작성 파일(코딩표, 스크립트, 결과표, 계산표): CC BY 4.0.
- Renewables.ninja CSV: CC BY-NC 4.0 (원 라이선스 유지).
- BADA2024, 해양공간관리계획 공간정보: 각 기관의 공공데이터 이용 조건에 따름. 출처 표기.
- IEA 데이터베이스에서 발췌한 필드는 IEA 이용약관에 따라 인용 목적으로만 포함. 원본은 IEA에서 받을 것.
- KIGAM 화면 캡처: 참고용, 원자료는 지오빅데이터 오픈플랫폼(https://data.kigam.re.kr).

## 변경 기록 / Changelog
- 2026-11-09: 수입 수소 도착 단가 산출 시트 추가(imported_hydrogen_delivered_cost_v1.xlsx). 코딩표 DEMO 소속값 0.6으로 통일, 27(AquaSector)·35(Dogger Bank) 비고 보완. 입지 v2(BADA·용도구역 재계산, 삼척 남부 외측 수심 점수 0.9→0.7). 비교 기준을 수입 분해수소 하나로 통일.
- 2026-10-26: 코딩표 최종(사유 변경 27→5, 30→2; 휴면 0.3 조정 26·36·37; 제외 8·14·28). LCOH v3(USD, 실측 시계열).
