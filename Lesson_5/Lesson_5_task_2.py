from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = driver.find_element(
        By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
