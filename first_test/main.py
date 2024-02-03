from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

default_width = 1400
default_height = 1000

service = Service(executable_path="C:/Users/jenif/Desktop/azulschool/python/tests/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.set_window_size(default_width, default_height)
wait = WebDriverWait(driver, 10)

driver.get('https://www.google.com/')
search_bar_google = wait.until(EC.presence_of_element_located((By.ID, 'APjFqb')))
search_bar_google.clear()
search_bar_google.send_keys('anime flv', Keys.ENTER)

link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "AnimeFLV")))
link.click()

search_bar_flv = wait.until(EC.presence_of_element_located((By.ID, "search-anime")))
search_bar_flv.send_keys('steins gate', Keys.ENTER)

movie = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/ul/li[4]/article/a')))
movie.click()
# movie_link = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/main/section[2]/ul/li/a')))
# driver.execute_script("arguments[0].scrollIntoView(true);", movie_link)
# movie_link.click()

time.sleep(10)
driver.quit()