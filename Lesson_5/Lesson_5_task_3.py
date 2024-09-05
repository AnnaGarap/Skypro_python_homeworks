from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    blue_button.click()
    sleep(2)
    driver.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    driver.quit()
