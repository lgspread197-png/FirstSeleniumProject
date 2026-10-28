#open browser
from selenium import webdriver
from selenium.webdriver.common.by import By
# selenium — библиотека для автоматизации браузера
# webdriver — инструмент, который позволяет Python управлять браузером.
# Импортируется сам WebDriver и класс By, который содержит стратегии поиска элементов

# главная цель — автоматизация браузера Google Chrome для поиска различных HTML-элементов на веб-странице
# с использованием разных стратегий поиска (селекторов)
# В твоём коде используются четыре основных способа:
# Способ	            Что означает	         Пример
# By.TAG_NAME	    По названию HTML-тега	      "h1"
# By.CSS_SELECTOR	  По CSS-селектору	  "h1", ".container"
# By.XPATH	        По XPath-выражению	     "//h1"
# By.CLASS_NAME	    По названию класса	    "container"

driver = webdriver.Chrome()
# webdriver.Chrome() — запускает браузер Chrome через Selenium.
# driver — переменная, в которой хранится объект управления браузером.
try:                # означает: «Попробуй выполнить этот блок кода».
    driver.get("https://telranedu.web.app/login")
# Если внутри блока произойдёт ошибка, Python остановит обычное выполнение блока
# и передаст управление подходящему except, если он есть.
    # driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")
    # driver.get("https://www.w3schools.com/css/css_table.asp")

# by TAG_NAME  (Поиск по названию тега (TAG_NAME))
    # поиск элементов сначала стандартным методом Selenium (By.ID)
    div = driver.find_elements(By.TAG_NAME,"div")
    # driver — управляет открытой страницей.
    # find_elements() — ищет все подходящие элементы.
    # By.TAG_NAME — ищет по названию HTML-тега.
    # "div" — название нужного тега.
# Результат сохраняется в переменную div (Если на странице 15 тегов <div>, то Selenium вернёт список из 15 элементов)
    # print(len(div))    # Функция len(div) выводит количество найденных блоков
    # Если ничего не найдено, вернётся пустой список [], а не ошибка поиска элемента.

    # поиск элементов через CSS-селекторы (By.CSS_SELECTOR) !!! фактический результат будет одинаковым !!!
    div2 = driver.find_element(By.CSS_SELECTOR,"div")
    div3 = driver.find_element(By.XPATH,"//div")
    # Поиск через XPath   -   //div означает поиск элементов div в любом месте HTML-документа.

    # find_elements (во множественном числе) ищет все теги <div> на странице и возвращает их списком (list)
    # Метод find_element (в единственном числе) находит только первый попавшийся на странице элемент
    # Поиск By.CSS_SELECTOR, "div" делает абсолютно то же самое, что и By.TAG_NAME, "div".

# Поиск элементов <h1> (заголовки страницы), <input> (HTML-тег поля ввода) и <a> (все ссылки)
    h1 = driver.find_element(By.TAG_NAME,"h1")
    h1_2 = driver.find_element(By.CSS_SELECTOR,"h1")
    h1_3 = driver.find_element(By.XPATH,"//h1")
    # print(h1.text)  # Чтобы посмотреть текст найденного заголовка
    # Если заголовок на странице — Login, то результат будет Login

    inputs = driver.find_elements(By.TAG_NAME,"input")
    input1 = driver.find_element(By.CSS_SELECTOR,"input")
    input1_1 =driver.find_element(By.XPATH,"//input")
    print(len(inputs))

    a_list = driver.find_elements(By.TAG_NAME,"a")
    # find_element returning .web
    a_list_1 = driver.find_elements(By.CSS_SELECTOR,"a")
    print(len(a_list))  #find_elements returning list
    a_list_2 = driver.find_elements(By.XPATH, "//a")

# by class  Поиск по названию класса (CLASS_NAME)
    # В HTML у элемента может быть атрибут class, который задаёт класс для CSS-стилей и позволяет находить элементы
    # по определённой группе или назначению (Здесь у div есть класс container)
    container = driver.find_element(By.CLASS_NAME, "container")  # runing by pairs class = container
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")  # "." searching only "container"
    #  в CSS-селекторах перед названием класса обязательно ставится точка (.container). В By.CLASS_NAME точка не нужна.

    container_2 = driver.find_element(By.XPATH, "//*[@class = 'container']")
    # // — искать по всему документу.
    # * — любой HTML-тег.
    # Символ @ в XPath используется для обращения к атрибуту
    # [@class = 'container'] — у элемента атрибут class должен точно равняться строке container.
    # эта команда найдёт элемент любого типа, если его атрибут class равен !ровно! container

    nav_bar = driver.find_elements(By.CLASS_NAME, "active")
    nav_bar_1 = driver.find_elements(By.CSS_SELECTOR, ".active")
    nav_bar_2 = driver.find_elements(By.XPATH, "//*[@class = 'active']")
    # By.XPATH, "//*[@class = 'active']"	ищет все элементы, у которых весь атрибут class равен active

    #print(len(nav_bar))
    #print(len(nav_bar_1))

    # Поиск по длинному названию класса
    login_1 = driver.find_element(By.CLASS_NAME, "login_login__3EHKB")
    login_1_1 = driver.find_elements(By.CSS_SELECTOR, ".login_login__3EHKB")
    login_1_1_1 = driver.find_elements(By.XPATH, "//*[@class = 'login_login__3EHKB']")

# By ID   Поиск по уникальному идентификатору (ID)
    root = driver.find_element(By.ID,"root")
    # Ищется главный блок приложения с id="root"
    root_1 = driver.find_elements(By.CSS_SELECTOR, "#root")
# В CSS-селекторах для поиска по ID используется символ решетки (#root)
    root_2 = driver.find_elements(By.ID, "root")
    root_3 = driver.find_elements(By.XPATH, "//*[@id = 'root']")
    #print(len(root_2))

    # By atribute   Поиск по атрибуту элемента
    name = driver.find_element(By.CSS_SELECTOR,"input[name=\"email\"]")
    email = driver.find_element(By.CSS_SELECTOR,"input[name=\"email\"]")
    email_xpath = driver.find_element(By.XPATH, "//input[@name = 'email']")
    # Это поиск поля для ввода электронной почты. Конструкция input[name="email"] говорит браузеру:
    # "Найди тег <input>, у которого атрибут name равен значению email".
    # Экранирование \" нужно, чтобы кавычки внутри строки не ломали код на Python.

    # subtitle = driver.find_element(By.CSS_SELECTOR,"[Type your data and hit Yalla!]")
    # start_sub = driver.find_element(By.CSS_SELECTOR,)

    # by text xPath
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_1_button = driver.find_element(By.XPATH, "//*[contains(text(),'Login')]")

    # by attribute
    input2 = driver.find_element(By.XPATH, "//input[@placeholder = 'Email']")
    # css
    # start CSS
    input3 = driver.find_element(By.CSS_SELECTOR, "[placeholder^='Em']")
    # start xPath
    input3_1 = driver.find_element(By.XPATH, "//*[starts-with(@placeholder,'Em')]")
    # end CSS
    input4 = driver.find_element(By.CSS_SELECTOR, "[placeholder$='il']")
    # end xPath (!не то! - Функция contains() проверяет, содержится ли строка где угодно внутри значения)
    input5 = driver.find_element(By.XPATH, "//*[contains(@placeholder,'il')]")
    # middle CSS
    input6 = driver.find_element(By.CSS_SELECTOR, "[placeholder *= 'ai']")
    # middle xPath
    input7 = driver.find_element(By.XPATH, "//*[contains(@placeholder,'ai')]")

    #xpath
    #parent
    div4 = driver.find_element(By.XPATH, "//h1/..")
    div5 = driver.find_element(By.XPATH, "//h1/parent::*") # то же самое попадаю вверх к div
    #ancestor
    div6 = driver.find_element(By.XPATH, "//h1/ancestor::div[2]") # все предки элемента

    ancestor = driver.find_elements(By.XPATH, "//h1/ancestor-or-self::*")
    for a in ancestor:
        print(a.tag_name)

    #ancestor-or-self
    ancestor = driver.find_elements(By.XPATH, "//h1/ancestor::*")
    for a in ancestor:
        print(a.tag_name)

    # linkText & partiaLinkText
    #home = driver.find_element(By.LINK_TEXT, "HOME")
    #home1 = driver.find_element(By.PARTIAL_LINK_TEXT, "  ....")  # часть слова в предложении

    # css in table
    # row
    # mexico = driver.find_element(By.CSS_SELECTOR, "#customers tr:nth-child(3)")
    # column
    # mexico1 = driver.find_element(By.CSS_SELECTOR, "#customers tr:nth-child(4)>td:nth-child(3)")
    # assert mexico.text == "Mexico"
    # first row
    # item = driver.find_element(By.CSS_SELECTOR, "#customers tr:first-child")
    # last row
    # italy = driver.find_element(By.CSS_SELECTOR, "#customers tr:last-child")

# #customers tr:nth-child(4)>td:last-child

finally:
    driver.quit()
    # Как бы ни завершился код внутри try (успешно или с ошибкой), этот блок сработает
    # и корректно закроет окно Chrome, освобождая оперативную память