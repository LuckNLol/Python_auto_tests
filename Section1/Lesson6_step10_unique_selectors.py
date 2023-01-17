from random_words import RandomWords
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

rw = RandomWords()
my_word = rw.random_word()

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/registration1.html")
    time.sleep(3)
    star_element1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    star_element1.send_keys(my_word)
    star_element2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    star_element2.send_keys(my_word)
    star_element3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    star_element3.send_keys(my_word)
    time.sleep(3)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(3)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text # конвертация полученного значения в текстовый формат
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()
