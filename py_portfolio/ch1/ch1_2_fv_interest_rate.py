# 오일러상수(e)를 제공받기 위해 import
import math

# amount : 원금, rate : 이자율
amount = 1
rate = 1.0

# 기간이 1인 경우, 즉 1년 복리 라면
n = 1
c_compound = amount * (1 + rate / n) ** n
print(c_compound)

# 기간 2인 경우, 즉 6개월 복리
n = 2
c_compound = amount * (1 + rate / n) ** n
print(c_compound)

# 기간 4인 경우, 즉 분기 복리
n = 4
c_compound = amount * (1 + rate / n) ** n
print(c_compound)

# 기간이 12이고, 월 복리일 경우
n = 12
c_compound = amount * (1 + rate / n) ** n
print(c_compound)

# 기간이 52인 경우, wn qhrfl dlf ruddn
n = 52
c_compound = amount * (1 + rate / n) ** n
print(c_compound)

n = 365
c_compound = amount * (1 + rate / n) ** n
print(c_compound)


# 매시간 복리
n = 8760
c_compound = amount * (1 + rate / n) ** n
print(c_compound)

# 매분 복리
n = 525600
c_compound = amount * (1 + rate / n) ** n
print(c_compound)

# 매초 복리
n = 31536000
c_compound = amount * (1 + rate / n) ** n
print(c_compound)
