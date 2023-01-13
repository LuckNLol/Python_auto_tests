import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calculation(x):
    return (math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/get_attribute.html")
    time.sleep(2)

    element_x = driver.find_element(By.CSS_SELECTOR, "img#treasure")
    x_value = element_x.get_attribute("x") #"valuex"
    print(x_value, type(x_value))
    x = x_value
    print(x)
    y = calculation(x)

    input_str = driver.find_element(By.CSS_SELECTOR, "#answer")
    input_str.send_keys(y)

    box_click = driver.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    box_click.click()

    rad_button_click = driver.find_element(By.CSS_SELECTOR, "input#robotsRule")
    rad_button_click.click()

    button_click = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button_click.click()

finally:
    time.sleep(5)
    driver.quit()