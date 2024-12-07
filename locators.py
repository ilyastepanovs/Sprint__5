from selenium.webdriver.common.by import By


class Locators:

    profile_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    logo = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']")
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")

    exit_button = (By.XPATH, "//button[text()='Выход']")

    login_button = (By.XPATH, "//button[text()='Войти в аккаунт']")
    email_input = (By.XPATH, "//label[text()='Email']//following::input[1]")
    password_input = (By.XPATH, "//input[@type='password']")
    submit_button = (By.XPATH, "//button[text()='Войти']")
    login_link = (By.XPATH, "//a[text()='Войти']")

    registration_link = (By.XPATH, "//a[text()='Зарегистрироваться']")
    name_input = (By.XPATH, "//label[text()='Имя']//following::input[1]")
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    invalid_password_error = (By.XPATH, ".//p[text()='Некорректный пароль']")

    sauces_tab = (By.XPATH, "//span[contains(text(),'Соусы')]")
    buns_tab = (By.XPATH, "//span[contains(text(),'Булки')]")
    filling_tab = (By.XPATH, "//span[contains(text(),'Начинки')]")
    sauces_tab_div = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")
    buns_tab_div = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")
    filling_tab_div = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")
