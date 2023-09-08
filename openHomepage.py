import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://swen17-geotech-team-c-frontend.vercel.app/')

time.sleep(3)
driver.close()

