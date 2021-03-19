
# 각 기간별 수익률 평균 구하기
returns = [0.1, 0.06, 0.05]

# 합계를 저장할 변수를 준비
sumOfReturn = 0.0

# 평균을 저장할 변수를 준비
arimean = 0.0
geomean = 1.0

# 기간별 수익률의 데이터 개수 구하기
n = len(returns)

# returns 리스트를 for 루프로 반복. 반복하는 동안 각 수익률을 변수 r로 받기
for r in returns:
    sumOfReturn = sumOfReturn + r

arimean = sumOfReturn / 3
print('AriMean is {:.2%}'.format(arimean))

# 기하평균 구하기
for r in returns:
    geomean = geomean * (1 + r)

# 기간 수익률로 변환
geomean = geomean ** (1/n) - 1

# 기하평균 출력
print('GeoMean is {:.2%}'.format(geomean))
