from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    for n in range(5):
        add_button = driver.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
    sleep(2)
    delete_buttons = driver.find_elements(
        By.XPATH, '//button[text()="Delete"]')
    print(
        f"Количество кнопок Delete на странице: {len(delete_buttons)}")
except Exception as ex:
    print(ex)
finally:
    driver.quit()
