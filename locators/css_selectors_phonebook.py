#open browser
from selenium import webdriver
from selenium.webdriver.common.by import By
# Этот код написан на Python с использованием библиотеки Selenium WebDriver
# Импортируется сам WebDriver и класс By, который содержит стратегии поиска элементов

# главная цель — автоматизация браузера Google Chrome для поиска различных HTML-элементов на веб-странице
# с использованием разных стратегий поиска (селекторов)
driver = webdriver.Chrome()
try:
    driver.get("https://telranedu.web.app/login")
    # driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")

    #by TAG_NAME  (Поиск по названию тега (TAG_NAME))
    # поиск элементов сначала стандартным методом Selenium (By.ID)
    div = driver.find_elements(By.TAG_NAME,"div")
    print(len(div))    # Функция len(div) выводит количество найденных блоков
    # поиск элементов через CSS-селекторы (By.CSS_SELECTOR) !!! фактический результат будет одинаковым !!!
    div2 = driver.find_element(By.CSS_SELECTOR,"div")
    #div3 = driver.find_element(By.XPATH,"div")

    # find_elements (во множественном числе) ищет все теги <div> на странице и возвращает их списком (list)
    # Метод find_element (в единственном числе) находит только первый попавшийся на странице элемент
    # Поиск By.CSS_SELECTOR, "div" делает абсолютно то же самое, что и By.TAG_NAME, "div".

    # Поиск элементов <h1> (заголовки страницы), <input> (поля ввода) и <a> (все ссылки)
    h1 = driver.find_element(By.TAG_NAME,"h1")
    h1_2 = driver.find_element(By.CSS_SELECTOR,"h1")

    input = driver.find_element(By.TAG_NAME,"input")
    input1 = driver.find_element(By.CSS_SELECTOR,"input")

    a_list = driver.find_elements(By.TAG_NAME,"a")
    # find_element returning .web
    a_list_1 = driver.find_elements(By.CSS_SELECTOR,"a")
    print(len(a_list))  #find_elements returning list

    # by class  Поиск по названию класса (CLASS_NAME)
    container = driver.find_element(By.CLASS_NAME, "container")  # runing by pairs class = container
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")  # searching only "container"
    #  в CSS-селекторах перед названием класса обязательно ставится точка (.container). В By.CLASS_NAME точка не нужна.
    nav_bar = driver.find_elements(By.CLASS_NAME, "active")
    nav_bar_1 = driver.find_elements(By.CSS_SELECTOR, ".active")
    print(len(nav_bar))
    print(len(nav_bar_1))
    login_1 = driver.find_element(By.CLASS_NAME, "login_login__3EHKB")
    login_1_1 = driver.find_elements(By.CSS_SELECTOR, ".login_login__3EHKB")

    # By ID   Поиск по уникальному идентификатору (ID)
    root = driver.find_element(By.ID,"root")
    # Ищется главный блок приложения с id="root"
    root_1 = driver.find_elements(By.CSS_SELECTOR, "#root")
    # В CSS-селекторах для поиска по ID используется символ решетки (#root)
    root_2 = driver.find_elements(By.ID, "root")
    print(len(root_2))

    # By atribute   Поиск по атрибуту элемента
    name = driver.find_element(By.CSS_SELECTOR,"input[name=\"email\"]")
    email = driver.find_element(By.CSS_SELECTOR,"input[name=\"email\"]")
    # Это поиск поля для ввода электронной почты. Конструкция input[name="email"] говорит браузеру:
    # "Найди тег <input>, у которого атрибут name равен значению email".
    # Экранирование \" нужно, чтобы кавычки внутри строки не ломали код на Python.

    # subtitle = driver.find_element(By.CSS_SELECTOR,"[Type your data and hit Yalla!]")
    # start_sub = driver.find_element(By.CSS_SELECTOR,)

finally:
    driver.quit()
    # Как бы ни завершился код внутри try (успешно или с ошибкой), этот блок сработает
    # и корректно закроет окно Chrome, освобождая оперативную память