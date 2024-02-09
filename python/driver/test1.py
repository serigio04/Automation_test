from selenium import webdriver;
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service(executable_path="C:/Users/jenif/Desktop/azulschool/python/tests/chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get("https://techwithtim.net")
print(driver.title)

select_theme = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div[2]/a[1]')))
select_theme.click()

try:    
    link_course = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div[3]/div[1]')))
    link_course.click()

    # link_course = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Python for complete beginners')))
    # link_course.click()
    link_course = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div[2]/div[1]')))
    link_course.click()

    course_overview = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div/div[1]/div[2]/p[1]')))
    print(course_overview.text)

    driver.back()
    driver.back()
    driver.back()

    driver.forward()
    driver.forward()

    wait()
except:
    driver.quit()
# try:
#     course_filter = driver.find_element_by_link_text('tag__TagContainer-sc-3f52y0-0 fPNUsx')
#     course_filter.click()
# except:
#     course_filter.click()