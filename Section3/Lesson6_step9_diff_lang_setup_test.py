import time

import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
lang = ["pl", "ru", "fr", "en-gb", "es"]

@pytest.mark.parametrize("language", lang)
def test_guest_should_see_login_link_pass(browser, language):
    browser.get(link)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "#login_link")



