import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
driver.get(link)
time.sleep(5)
try:
    button = driver.find_element_by_tag_name("button")
    _ = button.location_once_scrolled_into_view
    button.click()
finally:
    driver.quit()
    # или:
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()