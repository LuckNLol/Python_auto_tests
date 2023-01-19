import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_RegPage1_PyTest():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("http://suninjuly.github.io/registration1.html")
        star_element1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        star_element1.send_keys("Ivan")
        star_element2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        star_element2.send_keys("Ivanov")
        star_element3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        star_element3.send_keys("ivanov@mail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text  # конвертация полученного значения в текстовый формат
        assert ("Congratulations! You have successfully registered!") == (welcome_text)
    finally:
         browser.quit()

def test_RegPage2_PyTest():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get("http://suninjuly.github.io/registration2.html")
        star_element1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        star_element1.send_keys("Semen")
        star_element2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        star_element2.send_keys("Slepakov")
        star_element3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        star_element3.send_keys("semens@mail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text  # конвертация полученного значения в текстовый формат
        assert ("Congratulations! You have successfully registered!") == (welcome_text)
    finally:
        browser.quit()

# Необязательная запись
if __name__ == "__main__":
    pytest.main()