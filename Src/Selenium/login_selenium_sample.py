from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ウィンドウ非表示で実行
options = Options()
# options.add_argument('--headless')

browser = webdriver.Chrome('chromedriver.exe', options=options)

url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)

sleep(3)

elem_username = browser.find_element(By.ID, 'username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element(By.ID, 'password')
elem_password.send_keys('kohei')

elem_login_btn = browser.find_element(By.ID, 'login-btn')
elem_login_btn.click()

sleep(3)
browser.quit()
