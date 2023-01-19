import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(1)

driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(1)

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("get()")
time.sleep(1)

submit_button = driver.find_element(By.CSS_SELECTOR, "#submit_button")
time.sleep(2)

submit_button.click()
time.sleep(1)

driver.quit()