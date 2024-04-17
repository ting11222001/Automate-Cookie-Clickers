from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# wait for the language setting to appear
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()


cookie_id = "bigCookie"
cookies_id = "cookies"  # no. of cookies I have
# wait for the cookie to appear
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.ID, cookie_id))
)
cookie = driver.find_element(By.ID, cookie_id)

time.sleep(10)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text
    print(cookies_count)
