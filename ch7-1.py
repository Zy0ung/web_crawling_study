import requests
import bs4

URL = 'https://www.musinsa.com/ranking/best'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text, 'html.parser')
target = html.find('div', {'class' : 'right_contents hover_box'})
ranks = target.find_all("p", {'class' : 'list_info'})[:5]

for index in range(len(ranks)):
    title = ranks[index].text
    print(f"{index+1}위 {title}")
print()