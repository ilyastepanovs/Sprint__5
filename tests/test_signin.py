import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import STELLAR_BURGERS_URL
from locators import Locators
from data_helper import EMAIL, PASSWORD


@pytest.mark.usefixtures("driver")
class TestSignIn:

    def test_login_main_page(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.email_input).send_keys(EMAIL)
        driver.find_element(*Locators.password_input).send_keys(PASSWORD)
        driver.find_element(*Locators.submit_button).click()
        wait.until(EC.url_to_be(STELLAR_BURGERS_URL))
        assert driver.current_url == STELLAR_BURGERS_URL

    def test_login_profile(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(STELLAR_BURGERS_URL)
        driver.find_element(*Locators.profile_button).click()
        driver.find_element(*Locators.email_input).send_keys(EMAIL)
        driver.find_element(*Locators.password_input).send_keys(PASSWORD)
        driver.find_element(*Locators.submit_button).click()
        wait.until(EC.url_to_be(STELLAR_BURGERS_URL))
        assert driver.current_url == STELLAR_BURGERS_URL

    def test_login_registration_form(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(STELLAR_BURGERS_URL + "register")
        driver.find_element(*Locators.login_link).click()
        driver.find_element(*Locators.email_input).send_keys(EMAIL)
        driver.find_element(*Locators.password_input).send_keys(PASSWORD)
        driver.find_element(*Locators.submit_button).click()
        wait.until(EC.url_to_be(STELLAR_BURGERS_URL))
        assert driver.current_url == STELLAR_BURGERS_URL

    def test_login_password_recovery_form(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(STELLAR_BURGERS_URL + "forgot-password")
        driver.find_element(*Locators.login_link).click()
        driver.find_element(*Locators.email_input).send_keys(EMAIL)
        driver.find_element(*Locators.password_input).send_keys(PASSWORD)
        driver.find_element(*Locators.submit_button).click()
        wait.until(EC.url_to_be(STELLAR_BURGERS_URL))
        assert driver.current_url == STELLAR_BURGERS_URL
