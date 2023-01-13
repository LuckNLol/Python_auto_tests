import math
import pyperclip as pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calculation(x):
    return (math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    time.sleep(1)
    # Вместо назнвания окна можно использовать порядковый индекс окна начиная с базового
    first_window = browser.window_handles[0]
    # Переходим на следующее окно
    fly_button = browser.find_element(By.TAG_NAME, "button").click()
    # Инициализируем второе окно
    second_window = browser.window_handles[1]
    # Переключаем фокус с 1го на 2е окно
    browser.switch_to.window(second_window)

    # Выполняем необходимые операции
    value_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = value_x.text
    y = calculation(x)

    put_value_into_field = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    time.sleep(2)

    push_the_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    # Копируем код в буфер обмена из модального окна
    alert = browser.switch_to.alert
    alert_text = alert.text
    copyToClipboard = alert_text.split(": ")[-1]
    pyperclip.copy(copyToClipboard)
    time.sleep(2)
    alert.accept()

    # При необходимости можем переключиться обрано на исходное (или любое иное) окно
    browser.switch_to.window(first_window)

finally:
    time.sleep(3)
    browser.quit()