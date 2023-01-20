import pytest
from selenium import webdriver


@pytest.fixture(scope="function") # function, class, module, session
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()