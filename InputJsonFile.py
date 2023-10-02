import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://swen17-geotech-team-c-frontend.vercel.app/')
element = WebDriverWait(driver,5, 0.5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/section/section/aside/div[1]/ul/li[2]/div/span[1]")))
driver.find_element(By.XPATH, "/html/body/div[1]/section/section/section/aside/div[1]/ul/li[2]/div/span[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/section/section/section/aside/div[1]/ul/li[2]/ul/li[2]").click()
time.sleep(2)
upload_element=driver.find_element(By.XPATH,"/html/body/div/section/section/section/section/main/div/div[1]/div/div/div/div/div/div[1]/div[2]/span/div[1]/span/input")
file_path = "D:\\formState.json"
upload_element.send_keys(file_path)
time.sleep(5)
driver.close()