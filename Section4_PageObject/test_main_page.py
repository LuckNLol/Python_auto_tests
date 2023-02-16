import time
from selenium.webdriver.common.by import By

url = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    browser.get(url)
    time.sleep(3)
    go_to_login_page(browser)


