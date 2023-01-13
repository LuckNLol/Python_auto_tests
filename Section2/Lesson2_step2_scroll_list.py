import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/selects2.html")
    time.sleep(1)

    element1 = driver.find_element(By.CSS_SELECTOR, "span#num1")
    x = int(element1.text)
    element2 = driver.find_element(By.CSS_SELECTOR, "span#num2")
    y = int(element2.text)
    z = str(x+y)
    time.sleep(1)

    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)

    button_click = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    button_click.click()

finally:
    time.sleep(5)
    driver.quit()