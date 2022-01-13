#라이브러리 불러오기
import requests
import bs4

#웹 페이지를 열고 소스코드를 읽어오는 작업
req = requests.get("https://comic.naver.com/webtoon/weekday")

html = bs4.BeautifulSoup(req.text, 'html.parser')

#요일별 웹툰 영역 추출하기
columns = html.find_all('div',{'class':'col_inner'})

#요일별 top5 웹툰 제목 출력
for column in columns:
    day = column.find('h4').text
    webtoons = column.find_all('a', {'class' : 'title'})[:5]
    print(day)
    for index in range(len(webtoons)):
        title = webtoons[index].text
        print(f"{index+1}. {title}")
    print()