import math
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calculation(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) # задаем неявное ожидание (не портит код:) )
    # Развернуть браузер на всю ширину окна
    browser.maximize_window()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Установить явное ожидание и условие (цена = 100), следить за скобками (!!)
    good_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()

    # Скролл ниже по странице
    scroll_set = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", scroll_set)

    element_x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = element_x.text
    y = calculation(x)

    # Вводим результат уравнения в строку
    input_str = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_str.send_keys(y)

    # Жмем кнопку Submit
    submit_click = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

    # Копируем ответ из модального окна в буфер обмена
    alert = browser.switch_to.alert
    alert_text = alert.text
    copyToClipboard = alert_text.split(": ")[-1]
    pyperclip.copy(copyToClipboard)
    alert.accept()

finally:
    browser.quit()

