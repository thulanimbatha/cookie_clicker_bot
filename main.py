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

# find the right panel store
store = driver.find_elements(by=By.CSS_SELECTOR, value="#rightPanel #store div b")
# find each item within the store
store_items = [item.text for item in store]

del store_items[-1]
# for item in store_items:
#     cost = item.split("-")[1].strip()
#     print(cost)
items = [item.split(" - ") for item in store_items]
print(items)






