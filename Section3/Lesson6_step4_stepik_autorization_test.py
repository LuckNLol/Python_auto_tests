import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
          "https://stepik.org/lesson/236897/step/1]", "https://stepik.org/lesson/236898/step/1",
          "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
          "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

def time_calculation():
    return str(math.log(int(time.time())))

@pytest.mark.parametrize("email", link)
def test_stepik_login_link(browser, email):
    # Открыть страницу сайта
    browser.get(email)
    # Найти кнопку "Войти", нажать btn
    browser.find_element(By.CSS_SELECTOR, "#ember33").click()
    # Найти поле "E-mail"
    login = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    # Добавить в поле адрес почты
    login.send_keys("savonciel@yandex.ru")
    # Найти поле "Пароль"
    psw = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    # Ввести в поле psw
    psw.send_keys("savonciel")
    # Найти кнопку "Войти", нажать
    browser.find_element(By.XPATH, "//button[text()='Войти']").click()
    time.sleep(3)

    # Найти поле "Напишите свой ответ здесь", вставить полученное значение функции
    text_message = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
    text_message.send_keys(time_calculation())

    # Найти кнопку "Отправить", ДОЖДАТЬСЯ ПОКА КНОПКА СТАНЕТ КЛИКАБЕЛЬНОЙ, нажать
    send_btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    send_btn.click()

    # Сравнить полученные результаты
    fin_text = WebDriverWait(browser, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    graduate_text = fin_text.text
    assert "Correct!" == graduate_text
