from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

try:
    driver.get("https://the-internet.herokuapp.com/login")
    input_login = driver.find_element(By.ID, "username")
    sleep(2)
    input_login.send_keys("tomsmith")
    sleep(2)
    input_password = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(2)
    button_login = driver.find_element(By.TAG_NAME, "button")
    button_login.click()
    sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
