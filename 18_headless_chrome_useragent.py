from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True #headless -> 브라우저 띄우지 않고 동작
options.add_argument("window-size=1920x1080")
#headless쓸때 주의할 점. 안쓰면 Chrome -> headless Chrome 으로 user-agent떠서 때때로 차단될 수 있음
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")


browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()