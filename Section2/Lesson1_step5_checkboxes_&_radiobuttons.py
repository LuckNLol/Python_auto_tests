import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calculation(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/math.html")
    time.sleep(2)

    element_x = driver.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = element_x.text
    y = calculation(x)

    input_str = driver.find_element(By.CSS_SELECTOR, "#answer")
    input_str.send_keys(y)

    box_click = driver.find_element(By.XPATH, "//label[contains(text(),'the robot')]")
    box_click.click()

    rad_button_click = driver.find_element(By.CSS_SELECTOR, "input#robotsRule")
    rad_button_click.click()

    button_click = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button_click.click()

finally:
    time.sleep(10)
    driver.quit()