# 1. NPV

# 현금흐름을 cashflows 리스트에 저장한다.
# i는 햇수, r은 이자율

import numpy_financial as npf
import numpy as np
import scipy as sp
cashflows = [12000, 15000, 18000, 21000, 26000]
i = 0
r = 0.015

# 최초 투자 금액이며 현금 유출이므로 -로 표시
npv = -70000

# cashflows 리스트를 반복해 미래에 들어올 현금흐름을 할인함으로써 현재가치로 계산한 다음 npv변수에 누적
for c in cashflows:
    i = i+1
    npv = npv + c / (1 + r) ** i
print(npv)

# scipy로 npv 구현
cashflows = [-70000, 12000, 15000, 18000, 21000, 26000]
r = 0.015

# npv 함수로 순현재가치 계산
npv = npf.npv(r, cashflows)
print(npv)

# 2. IRR 구하기

cashflows = [-70000, 12000, 15000, 18000, 21000, 26000]

# irr함수
irr = npf.irr(cashflows)

# 구한 IRR을 NPV 할인율로 사용해 NPV를 구하기, IRR이 정확하다면 NPV는 0
npv = npf.npv(irr, cashflows)

# 결과 출력
print('IRR {0:.1%} makes NPV {1:.2f} '.format(irr, npv))
