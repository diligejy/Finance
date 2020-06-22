import requests
url = 'http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20200515002179&dcm_no=7343256&lang=ko'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
resp = requests.get(url, headers = {"user-agent": user_agent})
print(resp)
print(resp.content)