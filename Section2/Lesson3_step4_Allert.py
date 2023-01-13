import math
import pyperclip as pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calculation(x):
    return (math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/alert_accept.html")
    time.sleep(1)

    push_button = driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(1)

    alert = driver.switch_to.alert
    alert.accept()

    element_x = driver.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = element_x.text
    y = calculation(x)

    input_str = driver.find_element(By.CSS_SELECTOR, "#answer")
    input_str.send_keys(y)
    time.sleep(1)

    button_click = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    # добавляем наш код в буфер обмена
    alert = driver.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:

    time.sleep(5)
    driver.quit()
