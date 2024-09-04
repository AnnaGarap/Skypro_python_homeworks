from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

try:
    driver.get("https://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(driver, 5)
    modal_window = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(3)
    close_button.click()
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
