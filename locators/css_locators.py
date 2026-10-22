from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://telranedu.web.app/login")

# driver.close()  # only last tab will be closed
driver.quit()  # used to close whole process


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://telranedu.web.app/login")