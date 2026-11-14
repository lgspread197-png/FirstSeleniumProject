# python -m pip install pytest напиши код в терминале - это инсталляция библиотеки pytest
# pip list - узнать установленную версию 9.2.0
# python.exe -m pip install --upgrade pip   дополнительно (если есть проблемы)
# py -m install list  - или эту команду

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://telranedu.web.app/login"


def test_login():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)
        element = driver.find_element(By.NAME, 'email')
        assert element.is_displayed()

    finally:
        driver.quit()

def test_registration_button_is_displayed():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)

        button = driver.find_element(By.XPATH,"//button[text()='Registration']")
        assert button.is_displayed()

    finally:
        driver.quit()