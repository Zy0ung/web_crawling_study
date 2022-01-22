from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

URL = "https://papago.naver.com/"
driver.get(URL)

time.sleep(5)

driver.close()