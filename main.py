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
# no. of cookies I have generated
cookies_id = "cookies"

product_prefix = "product"
# no. of cookies required to buy a product
product_price_prefix = "productPrice"

# wait for the cookie to appear
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.ID, cookie_id))
)
cookie = driver.find_element(By.ID, cookie_id)

time.sleep(10)

while True:
    cookie.click()
    # cookies_count = driver.find_element(By.ID, cookies_id).text  # print: 262 cookies
    cookies_count = driver.find_element(
        By.ID, cookies_id).text.split(" ")[0]  # print: 262
    # remove the comma from the string for easy processing later
    cookies_count = int(cookies_count.replace(",", ""))
    # print(cookies_count)

    # check if I have enough cookie to buy products to generate more cookies
    for i in range(20):
        product_price = driver.find_element(
            By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)
        # print(product_price)

        # it will keep buying from the first product, cursor, until a cursor it more expensive than
        # the second product, grandma, so that it will start buying grandma
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break
