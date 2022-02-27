#1등부터 15등까지
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
# browser.find_element_by_class_name("Medal_button_more__2oy_Q").click()
# # browser.find_element_by_xpath("xpath복사해서 넣기").click() 이렇게도 가능
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,"lxml")

# with open("naver_oly4.html","w", encoding="utf-8") as f:
#     f.write(browser.page_source)
#     f.write(soup.prettify())

# # print("프로그램 저장완료")

# ol1 = soup.find("ol",{"class":"RankList_rank_list__1Ud5u"})
# li1 = ol1.find_all("li",{"class":"RankList_list_item__3qGhO"})
# # nation = li1.find("em").get_text()
# idx = 1
# for t in li1:
#     nation = t.find("em").get_text()
#     gold = t.find("div",{"class":"RankList_cell_gold__3_FoA RankList_is_selected__1mF87"})
#     silver = t.find("div",{"class":"RankList_cell_silver__MB0sW"})
#     bronze = t.find("div",{"class":"RankList_cell_bronze__3VT-9"})
#     total = t.find("div",{"class":"RankList_cell_total__3wDO1"})
#     print("[순위]:",idx)
#     print("국가명 : "+nation)
#     print("금메달 : "+gold.get_text())
#     print("은메달 : "+silver.get_text())
#     print("동메달 : "+bronze.get_text())
#     print("합계 : "+total.get_text())
#     idx+=1

   