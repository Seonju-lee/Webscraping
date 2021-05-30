from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")

#1.네이버 이동
browser.get("http://naver.com") #브라우저 객체를 통해 해당 url로 이동

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. id, pw 입력
browser.find_element_by_id("id").send_keys("lsj6787")
browser.find_element_by_id("pw").send_keys("내 네이버 pw")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

#5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("pjs6787")

#6. html 정보 출력
print(browser.page_source)

#7. 브라우저 종료
# brwoser.close() # 현재 탭만 종료
browser.quit() #전체 브라우저 종료

#이후 웹스크레핑 작업 가능