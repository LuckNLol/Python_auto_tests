from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
#Присваиваем переменной link url 
    link = "http://suninjuly.github.io/registration2.html"

#Присваиваем переменной browser вебдрайвер Chrome
    browser = webdriver.Chrome()
#Открываем url в браузере
    browser.get(link)
    time.sleep(5)
#Код для заполнения обязательных полей
    input1 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[1]/input")
    input1.send_keys("Andrey")
    input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[2]/input")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[3]/input")
    input3.send_keys("ivanov_a_b@bk.ru")
    time.sleep(5)
#Отправка заполненной формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
#Проверка регистрации, ожидание загрузки страницы
    time.sleep(10)

#Поиск элемента содержащего текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

#Запись в переменную welcome_test из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

#Проверка с помощью assert, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
#Задержка для визуальной оценки результатов прохождения скрипта
    time.sleep(5)
#Закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

