import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.get("https://staging.thecloudgate.io/member/login")

driver.find_element(By.NAME,'loginId').send_keys('cgtestst02')
driver.find_element(By.NAME,'password').send_keys('!twc1234')

driver.find_element(By.XPATH,'//*[@id="login"]/div/div/div[3]/div[1]/div/button').click()
