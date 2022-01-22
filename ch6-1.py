import requests

URL = 'https://www.musinsa.com/ranking/best'
raw = requests.get(URL)

#print(raw) # 요청 성공 여부 출력
print(raw.text) # HTML 코드 출력