import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://telranedu.web.app/login"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)

    yield driver

    driver.quit()

def test_registration(driver):
    driver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("manuel@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("Manuel12345$")
    driver.find_element(By.XPATH, "//button[text()='Registration']").click()

