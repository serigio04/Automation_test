from selenium import webdriver;
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service(executable_path="C:/Users/jenif/Desktop/azulschool/python/tests/chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))
cookie_count = wait.until(EC.presence_of_element_located((By.ID, "coockies")))
items = [wait.until(EC.presence_of_element_located((By.ID, "productPrice" + str(i)))) for i in range (1,-1,-1)]
         
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = int(cookie_count.tect.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
