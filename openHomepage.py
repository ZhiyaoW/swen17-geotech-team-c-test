import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

time.sleep(3)

driver.close()