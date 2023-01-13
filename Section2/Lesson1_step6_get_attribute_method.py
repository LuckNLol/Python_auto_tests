import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/math.html")
    time.sleep(2)

    people_radio_button = driver.find_element(By.ID, "peopleRule")
    people_checked = people_radio_button.get_attribute("checked")
    print("Value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default" или (см.ниже)
    assert people_checked == "true", "People radio is not selected by default"
    time.sleep(10)

    robots_radio_button = driver.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio_button.get_attribute("checked")
    print("Value of people radio: ", robots_checked)
    assert robots_checked is None

    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
    disabled_check = submit_button.get_attribute("disabled")
    # 'None' по умолчанию, по истечении 8сек = 'true'
    print("Value of ""Supmit"" button: ", disabled_check)


finally:
    time.sleep(4)
    driver.quit()