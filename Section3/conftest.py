import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# pytest_addoption и фикстура request (хотим показать, как можно настраивать тестовые окружения
# с помощью передачи параметров через командную строку или интерпритатор)

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome of firefox")
    # default=None или "chrome" или "firefox" (Регистр важен!). Менять браузер можно тут или ниже.
    parser.addoption("--language", action="store", default=None, help="Choose language: ru, en, ...(etc)")

# КОГДА НУЖНО ИМПЛЕМЕНТИРОВАТЬ НЕСКОЛЬКО БРАУЗЕРОВ
@pytest.fixture(scope="function") # function, class, module, session
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", user_language)
        print("\nstart Firefox browser for test..")
        browser = webdriver.Firefox()   # ??? (options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


# КОНСТРУКЦИЯ ДЛЯ ОДНОГО БРАУЗЕРА
# @pytest.fixture(scope="function")  # function, class, module, session
# def browser():
    # для Chrome в PyCharm
    # print("\nstart Chrome browser for test..")
    # browser = webdriver.Chrome()

    # browser.implicitly_wait(10)
    # browser.maximize_window()
    # yield browser
    # print("\nquit browser..")
    # browser.quit()