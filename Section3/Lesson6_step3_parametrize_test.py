import time

import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# из файла cnftest.py передаём фикстуру browser в тест, а также парамерт language
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login(browser):
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        pass