
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
try:
    driver.get("https://demowebshop.tricentis.com/")

    div = driver.find_elements(By.XPATH, "//div")
    print(len(div))
    contains_class = driver.find_elements(By.XPATH, "//*[contains(@class,'front')]")
    print(len(contains_class))
    input_ = driver.find_elements(By.XPATH, "//input[@class='search-box-text ui-autocomplete-input']")
    print(len(input_))
    hrev = driver.find_elements(By.XPATH, "//a[@href='/books']")
    print(len(hrev))
    a_ = driver.find_elements(By.XPATH, "//a")
    print(len(a_))
    script = driver.find_elements(By.XPATH, "//script")
    print(len(script))
    print()

    master_wrapper_page = driver.find_elements(By.XPATH, "//*[@class='master-wrapper-page']")
    print(len(master_wrapper_page))
    header = driver.find_elements(By.XPATH, "//*[@class ='header']")
    print(len(header))
    pollanswers_1 = driver.find_elements(By.XPATH, "//input[@id='pollanswers-1']")
    print(len(pollanswers_1))
    print()

    dialog_notifications_success = driver.find_elements(By.XPATH, "//*[@id='dialog-notifications-success']")
    print(len(dialog_notifications_success))
    dialog_notifications_error = driver.find_elements(By.CSS_SELECTOR, "dialog-notifications-error")
    print(len(dialog_notifications_error))
    dialog_notifications_error1 = driver.find_elements(By.XPATH, "//*[@id='dialog-notifications-error']")
    print(len(dialog_notifications_error1))
    print()

    image = driver.find_element(By.XPATH,"//div[@class='picture']//img[@title='Show details for Build your own cheap computer']")
    javascript = driver.find_element(By.XPATH,"//body[1]/div[4]/div[1]/script[1]")
    li = driver.find_element(By.XPATH,"//li/parent::*")
    li_2 = driver.find_element(By.XPATH,"(//li[@class='answer'])[1]")
    h2 = driver.find_element(By.XPATH,"(//h2)[4]")


finally:
    driver.quit()