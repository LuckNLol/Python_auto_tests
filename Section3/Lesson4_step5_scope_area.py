import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope='class') # Браузер откроется один раз для каждого тестового Класса (независимо от кол.функций)
# @pytest.fixture(scope='function') # Браузер откроется/закроется столько раз сколько функций будет в классе/классах
# @pytest.fixture(scope='module') # Браузер откроется один раз выполнит все тесты в каждом классе и закроется
# @pytest.fixture(scope='session') # Браузер откроется один раз выполнит все тесты в каждом классе и закроется
def browser():
    print("\nЗапуск браузера для теста...")
    browser = webdriver.Chrome()
    yield browser
    print("\nБраузер закрывается...")
    browser.quit()

class TestMainPage1():
    # Вызов текстуры и передача ее как параметра
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")