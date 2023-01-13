from random_words import RandomWords
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

rw = RandomWords()
my_word = rw.random_word()

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # star_elements = browser.find_elements(By.XPATH, "//label[contains(text(),'*')]")
    star_elements = browser.find_elements(By.CSS_SELECTOR, "div.container form:nth-child(3) > div.first_block input")
    for element in star_elements:
        element.send_keys(my_word)
    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text # конвертация полученного значения в текстовый формат
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()
