from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from urls import STELLAR_BURGERS_URL
from data_helper import EMAIL, PASSWORD


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(STELLAR_BURGERS_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    wait = WebDriverWait(driver, 10)
    driver.find_element(*Locators.login_button).click()
    driver.find_element(*Locators.email_input).send_keys(EMAIL)
    driver.find_element(*Locators.password_input).send_keys(PASSWORD)
    driver.find_element(*Locators.submit_button).click()
    wait.until(EC.url_to_be(STELLAR_BURGERS_URL))
