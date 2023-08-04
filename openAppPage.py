import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get('https://swen17-geotech-team-c-frontend.vercel.app/')

element=WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located(By.XPATH,"/html/body/div/div/header/ul/li[2]"))
driver.find_element(By.XPATH, "/html/body/div/div/header/ul/li[2]").click()
time.sleep(3)
driver.close()