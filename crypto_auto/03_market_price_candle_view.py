# 시세 캔들 조회
import pyupbit

# 1분봉 조회
# df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
# print(df)

# 3분봉 조회
# df = pyupbit.get_ohlcv("KRW-BTC", "minute3")
# print(df)

# 5분봉 조회
# df = pyupbit.get_ohlcv("KRW-BTC", "minute5")
# print(df)

# 1분봉으로 3분봉 만들기
df = pyupbit.get_ohlcv("KRW-BTC", "minute1")

df['open'] = df['open'].resample('3T').first()
df['high'] = df['high'].resample('3T').max()
df['low'] = df['low'].resample('3T').min()
df['close'] = df['close'].resample('3T').last()
df['volume'] = df['volume'].resample('3T').sum()

print(df)
