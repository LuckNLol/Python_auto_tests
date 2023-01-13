from random_words import RandomWords
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

rw = RandomWords()
my_word = rw.random_word()

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(my_word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

# except Exception():
#     print("Some error happened")
finally:
    time.sleep(10)
    browser.quit()