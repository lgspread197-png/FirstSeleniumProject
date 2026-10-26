# В FirstSeleniumProject создайте новый тестовый класс и в нем тестовый метод,
# который найдет по тэгу 10 элементов на https://demowebshop.tricentis.com/
# с использованием стратегии By.NAME , By.CLASS_NAME , By.ID  и By.CSS_SELECTOR

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
try:
    driver.get("https://demowebshop.tricentis.com/")

    div = driver.find_elements(By.TAG_NAME, "div")
    print(len(div))
    ul = driver.find_elements(By.TAG_NAME, "ul")
    print(len(ul))
    input = driver.find_elements(By.CSS_SELECTOR, "input")
    print(len(input))
    hrev = driver.find_elements(By.CSS_SELECTOR, 'a[href="/books"]')
    print(len(hrev))
    a_ = driver.find_elements(By.CSS_SELECTOR, "a")
    print(len(a_))
    script = driver.find_elements(By.TAG_NAME, "script")
    print(len(script))
    print()

    master_wrapper_page = driver.find_elements(By.CLASS_NAME, "master-wrapper-page")
    master_wrapper_page_1 = driver.find_elements(By.CSS_SELECTOR, ".master-wrapper-page")
    print(len(master_wrapper_page))
    header = driver.find_elements(By.CLASS_NAME, "header")
    print(len(header))
    footer = driver.find_elements(By.CSS_SELECTOR, "footer")
    print(len(footer))
    print()

    dialog_notifications_success = driver.find_elements(By.ID, "dialog-notifications-success")
    print(len(dialog_notifications_success))
    dialog_notifications_error = driver.find_elements(By.CSS_SELECTOR, "dialog-notifications-error")
    print(len(dialog_notifications_error))
    dialog_notifications_error1 = driver.find_elements(By.ID, "dialog-notifications-error")
    print(len(dialog_notifications_error1))
    print()

    # NewsletterEmail = driver.find_element(By.CSS_SELECTOR,"input[newsletter-email=\"NewsletterEmail\"]")
    # print(len(NewsletterEmail))
    # "Найди тег <input>, у которого атрибут NewsletterEmail равен значению "NewsletterEmail".    пишет ошибку не пойму
    # не до конца разобрался с поиском по атрибуту элемента

finally:
    driver.quit()