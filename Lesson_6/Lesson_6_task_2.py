from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    input_button_name = driver.find_element(
        By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
    confirm_button_name = driver.find_element(
        By.CSS_SELECTOR, "#updatingButton").click()
    print(driver.find_element(
            By.CSS_SELECTOR, "#updatingButton").text)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
