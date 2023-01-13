from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link_num = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(link_num) # 224595

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")
    link = browser.find_element(By.PARTIAL_LINK_TEXT, link_num)
    time.sleep(2)
    link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)
except Exception():
    print("Some error happened")
finally:
    browser.quit()