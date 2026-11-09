# fsQCA 실행 스크립트 v3 — 본 분석 44건(제외 후보 3건 제외), 강건성 47건. 입력 fsqca_input_v2.csv
# 설치(처음 한 번): install.packages("QCA")
library(QCA)

# 1. 데이터 읽기 ----------------------------------------------------------
d <- read.csv("fsqca_input_v2.csv", fileEncoding = "UTF-8-BOM")
# 조건: ONSHORE(육상 수전해) PORT(산단·항만 입지) GRID(계통 접속)
#       OFFTAKE(전용 수요처: 없음0/MOU0.33/계약1) LOCAL(현지1/배관0.55/수출0)
#       SMALL(<50MW 1 / 50~200 0.67 / 200~1000 0.33 / >=1GW 0) SUPPORT(공적 지원)
# 결과: OUT(성립 소속값: 가동1/FID0.9/DEMO0.6/보류0.4/휴면0.3/취소0)
conds <- c("ONSHORE","PORT","GRID","OFFTAKE","LOCAL","SMALL","SUPPORT")

# 본 분석 표본: 제외 후보(HEAL·Lowestoft·Mukran) 뺀 44건. 47건은 강건성
d47 <- d; d <- subset(d, exclude_candidate == 0); d45 <- d47

# 2. 필요조건 검정 -------------------------------------------------------
# 일관성(inclN) >= 0.9 이고 피복도(covN)가 너무 낮지 않으면 필요조건 후보
d$NOUT <- 1 - d$OUT; d45$NOUT <- 1 - d45$OUT          # 결과 부정(중단) 열
print(pof(d[, conds], outcome = "OUT",  data = d, relation = "necessity"))
# 결과 부정(중단)의 필요조건
print(pof(d[, conds], outcome = "NOUT", data = d, relation = "necessity"))
# 조건 부정의 필요조건(예: ~SMALL이 중단의 필요조건인지)
nc <- 1 - d[, conds]; names(nc) <- paste0("n", conds)
print(pof(nc, outcome = "NOUT", data = d, relation = "necessity"))

# 3. 진리표 ---------------------------------------------------------------
# incl.cut: 일관성 기준 0.8, n.cut: 행당 최소 사례 수(중간 N이므로 2 권장; 1로도 비교)
tt1 <- truthTable(d, outcome = "OUT", conditions = conds,
                  incl.cut = 0.75, n.cut = 2, pri.cut = 0.5,
                  show.cases = TRUE, sort.by = "OUT, n")
print(tt1)

# 4. 최소화: 세 가지 해 ----------------------------------------------------
sol_c <- minimize(tt1, details = TRUE)                         # 복잡해(conservative)
sol_p <- minimize(tt1, include = "?", details = TRUE)          # 절약해(parsimonious)
# 중간해: 방향 가정(dir.exp) — 각 조건이 '있을 때' 성립에 기여한다고 가정
sol_i <- minimize(tt1, include = "?", details = TRUE,
                  dir.exp = c(ONSHORE = 1, PORT = 1, GRID = 1, OFFTAKE = 1,
                              LOCAL = 1, SMALL = 1, SUPPORT = 1))
print(sol_c); print(sol_p); print(sol_i)

# 5. 결과 부정(중단) 분석 — 비대칭성 때문에 따로 실행 ---------------------
tt0 <- truthTable(d, outcome = "NOUT", conditions = conds,
                  incl.cut = 0.75, n.cut = 2, pri.cut = 0.5, show.cases = TRUE)
print(tt0)
sol0_i <- try(minimize(tt0, include = "?", details = TRUE,
                   dir.exp = c(ONSHORE = 0, PORT = 0, GRID = 0, OFFTAKE = 0,
                               LOCAL = 0, SMALL = 0, SUPPORT = 0)))
print(sol0_i)

# 6. 강건성 점검 -----------------------------------------------------------
# (a) 일관성 기준 0.75 / 0.85
for (ic in c(0.8, 0.85)) {
  tt <- truthTable(d, outcome = "OUT", conditions = conds, incl.cut = ic, n.cut = 2)
  cat("\n--- incl.cut =", ic, "---\n"); print(try(minimize(tt, include = "?", details = TRUE)))
}
# (b) 빈도 기준 1
tt_n1 <- truthTable(d, outcome = "OUT", conditions = conds, incl.cut = 0.75, n.cut = 1)
print(try(minimize(tt_n1, include = "?", details = TRUE)))
# (c) 제외 후보 포함 47건
tt47 <- truthTable(d47, outcome = "OUT", conditions = conds, incl.cut = 0.75, n.cut = 2)
print(try(minimize(tt47, include = "?", details = TRUE)))
# (d) 휴면·보류 제외(취소/성립만) 
d_strict <- subset(d, !(status %in% c("Dormant","On hold")))
tt_s <- truthTable(d_strict, outcome = "OUT", conditions = conds, incl.cut = 0.75, n.cut = 2)
print(try(minimize(tt_s, include = "?", details = TRUE)))

# 7. XY 산점도(PDF로 저장) ------------------------------------------------
pdf("xyplot_offtake.pdf"); try(XYplot(d$OFFTAKE, d$OUT, relation = "sufficiency", xlab="OFFTAKE", ylab="OUT")); dev.off()
cat("\n완료: result 파일과 xyplot_offtake.pdf 확인\n")
