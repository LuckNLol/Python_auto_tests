import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope='function', autouse=True)
def browser():
    print("\nЗапуск браузера для теста...")
    browser = webdriver.Chrome()
    yield browser
    print("\nБраузер закрывается...")


class TestMainPage1():
    # Вызов текстуры и передача ее как параметра
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
