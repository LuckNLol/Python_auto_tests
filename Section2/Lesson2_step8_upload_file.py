import os.path

from random_words import RandomWords
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/file_input.html")
    time.sleep(1)

    first_name = driver.find_element(By.CSS_SELECTOR, "[name=firstname]")
    first_name.send_keys("Vasiliy")
    last_name = driver.find_element(By.CSS_SELECTOR, "[name=lastname]")
    last_name.send_keys("Vasilisyn")
    email_element3 = driver.find_element(By.CSS_SELECTOR, "[name=email]")
    email_element3.send_keys("Vasiliy@gjamal.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "short_bio.txt"
    file_path = os.path.join(current_dir, file_name)
    element4 = driver.find_element(By.CSS_SELECTOR, "[type='file']")
    element4.send_keys(file_path)

    push_submit = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    push_submit.click()

finally:
    time.sleep(5)
    driver.quit()
