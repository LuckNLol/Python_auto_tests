import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"), 'Button not found'
    assert button is not None, 'OMG, Button not found!'
