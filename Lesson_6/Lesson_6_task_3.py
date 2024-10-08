from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 40)

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    waiter.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#text"), "Done!"))
    get_attribute = driver.find_element(
        By.CSS_SELECTOR, "#award").get_attribute("src")
    print(get_attribute)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
