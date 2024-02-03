from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="C:/Users/jenif/Desktop/azulschool/python/tests/chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get('https://www.google.com/')
search_bar = wait.until(EC.presence_of_element_located((By.ID, 'APjFqb')))
search_bar.clear()
search_bar.send_keys('anime', Keys.ENTER)

# expected_result = '"manga"'
# actual_result = driver.find_element(By.XPATH, "//div[@class='PZPZlf ssJ7i B5dxMb']")

time.sleep(5)

# assert expected_result == actual_result, f'Error. Expected result {expected_result}, and actual result is {actual_result}'

