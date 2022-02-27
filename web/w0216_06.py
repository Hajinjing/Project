import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('./chromedriver')
url = 'https://m.sports.naver.com/beijing2022/medal/index'
browser.get(url)

time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")

with open("naver_oly3.html","w", encoding="utf-8") as f:
    # f.write(browser.page_source)
    f.write(soup.prettify())

print("프로그램 저장완료")



# url = 'https://m.sports.naver.com/beijing2022/medal/index'
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

