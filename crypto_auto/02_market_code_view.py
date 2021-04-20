# 마켓코드 조회
import pyupbit

# 1. get_tickers 함수
# 마켓 코드를 리스트 타입으로 리턴
# tickers = pyupbit.get_tickers()
# print(tickers)
# print(len(tickers))

# 2. 시장 지정하여 특정 시장 마켓 코드 조회
tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)
print(len(tickers))

# 연습문제 - 비트코인 시장의 마켓 코드를 pyupbit로 얻어온 후 목록과 개수출력
tickers = pyupbit.get_tickers(fiat="BTC")
print(tickers)
print(len(tickers))
