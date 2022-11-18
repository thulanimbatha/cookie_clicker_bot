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

index = 0

interval_check = time.time() + 5

# TODO Finish final part of project - adding in the click counter, stopping game after 5 minutes

while True:
    cookie.click()

    # check every 10 seconds
    if time.time() > interval_check:

        # find the right panel store
        store = driver.find_elements(by=By.CSS_SELECTOR, value="#rightPanel #store div b")
        
        # find each item within the store
        store_items = [item.text for item in store]
        
        # delete useless item
        if store_items[-1] == "":
            del store_items[-1] 
        
        # get the split items
        
        items = [item.split(" - ") for item in store_items]
        
        # get the costs
        costs = [item[1] for item in items]
        for cost in costs:
            if cost != "":
                cost.replace(",", "")

        points = driver.find_element(by=By.ID, value="money").text
        if points != "":
            points.replace(",", "")

        if int(points) > int(costs[index]):
            # click on highest affordable element
            store[index].click()
            # move onto next item in store
            index += 1





