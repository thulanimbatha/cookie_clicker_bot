from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url="https://orteil.dashnet.org/cookieclicker/")

# find the cookie
cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookieAnchor #bigCookie")

