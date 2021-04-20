import pyupbit

with open('api.txt', 'r') as f:
    keys = f.readlines()

access, secret = keys[0].strip('\n'), keys[1]
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
