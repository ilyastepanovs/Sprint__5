from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators

from data_helper import get_random_email, get_random_password


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def registration_data():
    name = "Илья"
    email = get_random_email()
    return name, email


@pytest.fixture
def valid_random_pass():
    password = get_random_password()
    return password


@pytest.fixture
def invalid_random_pass():
    password = get_random_password(False)
    return password


@pytest.fixture
def login(driver):
    email = "ilyastepanov131989@yandex.ru"
    password = "123456"
    wait = WebDriverWait(driver, 10)

    driver.find_element(*Locators.login_button).click()
    driver.find_element(*Locators.email_input).send_keys(email)
    driver.find_element(*Locators.password_input).send_keys(password)
    driver.find_element(*Locators.submit_button).click()

    wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))