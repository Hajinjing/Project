from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
 
from selenium.webdriver.common.by import By #출력화면 대기 메소드
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #브라우저 화면의 상태를 알려주는 메서드


browser = webdriver.Chrome('./chromedriver')
browser.maximize_window() #윈도우 창 최대화
url = 'https://flight.naver.com/'
browser.get(url)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[1]').click()

time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click()

#날짜 창 열기
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
#가는날
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/button').click()
time.sleep(2)
#오는날
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[3]/button').click()

#인원선택창
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[3]/button').click()
# time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[3]/div/div[1]/div[1]/button[2]').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[5]')))
time.sleep(10)
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    # 현재 높이에서 브라우저 최대높이까지 스크롤해서 내림.
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 데이터가 나타날때까지 대기하고 있음.
    time.sleep(2)
    # 화면을 스크롤해서 내려온 화면높이를 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 현재높이와 이전높이가 같은지 비교해서 같으면 더이상 스크롤이 없으므로 빠져 나옴.
    if curr_height == prev_height:
        break
    # 현재높이를 이전높이에 적용하고 계속적으로 반복
    prev_height = curr_height


# 스크롤을 내리는 명령어를 넣어야 함.

# 출력
# 브라우저 페이지 소스 가져옴.
page_url = browser.page_source

soup = BeautifulSoup(page_url,"lxml")
flights = soup.find_all("div",{"class":"result"})

for flight in flights:
    
    print("항공사 : "+flight.b.get_text())
    pirnt("")

# print("검색 된 항공권 개수 : ",len(flights))
