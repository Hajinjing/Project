from selenium import webdriver
from selenium.webdriver.common.keys import Keys #키보드 관련 메소드
import time #시간 지연
import random #지연시간을 랜덤으로 처리


browser = webdriver.Chrome('./chromedriver')
browser.get("http://www.naver.com")

browser.find_element_by_class_name("link_login").click()
time.sleep(3)
#자바스크립트로 id,pw를 inputbox에 입력
input_js = '\
    document.getElementById("id").value="{id}"; \
    document.getElementById("pw").value="{pw}";\
    '.format(id="yk234589",pw="gkwlswkd!159")
time.sleep(random.uniform(1,3)) #3초 시간 지연

browser.execute_script(input_js)
time.sleep(2)
# elem = browser.find_element_by_id("id")
# elem.send_keys("yk234589")
# time.sleep(3) #3초 시간 지연

# elem = browser.find_element_by_id("pw")
# elem.send_keys("gkwlswkd!159")
# time.sleep(2)

browser.find_element_by_id("log.login").click()




