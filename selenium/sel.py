""" from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("")

time.sleep(6)
X_path = "/html/body/main/div[1]/div/form/input"
search_box = driver.find_element(By.XPATH, X_path)
search_box.send_keys("pandas")
search_box.send_keys(Keys.ENTER)

time.sleep(40) """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()


print(type(driver))
driver.get("https://quotes.toscrape.com/login")
time.sleep(10)
username = driver.find_element(By.XPATH, "/html/body/div/div")
username.send_keys("abcd")
time.sleep(15)