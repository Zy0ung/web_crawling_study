from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

URL = "https://papago.naver.com/"
browser.get(URL)
time.sleep(3)

Worddict = {}

while True:
    word = input("번역 할 영단어를 입력하세요.(0을 입력하면 종료됩니다.) : ")

    if word == '0':
        break
     
    form = browser.find_element_by_css_selector("textarea#txtSource")
    form.send_keys(word)

    button = browser.find_element_by_css_selector("button#btnTranslate")
    button.click()
    time.sleep(2)

    result = browser.find_element_by_css_selector("div#txtTarget")
    Worddict[word] = result.text
    
    form.clear()

print(Worddict)
browser.close()
