import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calculation(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    # driver.set_window_size(1280, 960)
    driver.get("http://SunInJuly.github.io/execute_script.html")
    time.sleep(1)

    element_x = driver.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = element_x.text
    y = calculation(x)

    input_str = driver.find_element(By.CSS_SELECTOR, "#answer")
    input_str.send_keys(y)

    scroll_set = driver.find_element(By.CSS_SELECTOR, "#answer")
    driver.execute_script("return arguments[0].scrollIntoView(true);", scroll_set)

    check_box_click = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_box_click.click()

    radio_button_click = driver.find_element(By.CSS_SELECTOR, "input#robotsRule")
    radio_button_click.click()

    button_click = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button_click.click()


finally:
    time.sleep(5)
    driver.quit()