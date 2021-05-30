from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) #url로 이동
#가는날 선택
browser.find_element_by_link_text("가는날 선택").click()

#이번달 30일,31일 선택
# browser.find_elements_by_link_text("30")[0].click() #[0] -> 이번달
# browser.find_elements_by_link_text("31")[0].click() #[0] -> 이번달  
#다음날 29일, 30일 선택
browser.find_elements_by_link_text("29")[0].click() #[0] -> 다음달 (첫번째 29일이 다음달이라서) 
browser.find_elements_by_link_text("30")[1].click() #[1] -> 다음달

#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

#Xpath(해당 elem)나올때까지 최대 10초까지 로딩 기다려라
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))
    #성공했을 때 동작 수행
    print(elem.text) #첫번째 결과 출력
finally:
    browser.quit()

#첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)