from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

# find the cookie
cookie = driver.find_element(by=By.ID, value="cookie")





