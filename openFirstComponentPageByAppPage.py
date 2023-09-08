import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://swen17-geotech-team-c-frontend.vercel.app/')
element = WebDriverWait(driver, 3, 0.5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/aside/div[1]/ul/li[2]")))
driver.find_element(By.XPATH, "/html/body/div/div/div/div/aside/div[1]/ul/li[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div/aside/div[1]/ul/li[2]/ul/li[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/main/div/div[2]/div/div/div[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/main/div/div[2]/div/div/div[2]/div[2]/div[3]/button").click()
time.sleep(3)
driver.close()