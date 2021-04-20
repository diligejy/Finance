# 원화시장에서만 거래 가능한 마켓코드 리스트로 저장
import requests

url = "https://api.upbit.com/v1/market/all"

querystring = {"isDetails": "true"}

response = requests.request("GET", url, params=querystring)

data = response.json()
krw_list = []
for ticker in data:
    if ticker['market'].startswith("KRW"):
        krw_list.append(ticker['market'])

print(krw_list)
print(len(krw_list))
