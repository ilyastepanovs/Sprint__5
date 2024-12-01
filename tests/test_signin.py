import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.mark.usefixtures("driver")
class TestSignIn:
    MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"
    EMAIL = "ilyastepanov131989@yandex.ru"
    PASSWORD = "123456"

    def test_login_main_page(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.email_input).send_keys(self.EMAIL)
        driver.find_element(*Locators.password_input).send_keys(self.PASSWORD)
        driver.find_element(*Locators.submit_button).click()
        wait.until(EC.url_to_be(self.MAIN_PAGE_URL))
        assert driver.current_url == self.MAIN_PAGE_URL

    def test_login_profile(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(self.MAIN_PAGE_URL)
        driver.find_element(*Locators.profile_button).click()
        driver.find_element(*Locators.email_input).send_keys(self.EMAIL)
        driver.find_element(*Locators.password_input).send_keys(self.PASSWORD)
        driver.find_element(*Locators.submit_button).click()
        wait.until(EC.url_to_be(self.MAIN_PAGE_URL))
        assert driver.current_url == self.MAIN_PAGE_URL

    def test_login_registration_form(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(self.MAIN_PAGE_URL + "register")
        driver.find_element(*Locators.login_link).click()
        driver.find_element(*Locators.email_input).send_keys(self.EMAIL)
        driver.find_element(*Locators.password_input).send_keys(self.PASSWORD)
        driver.find_element(*Locators.submit_button).click()
        wait.until(EC.url_to_be(self.MAIN_PAGE_URL))
        assert driver.current_url == self.MAIN_PAGE_URL

    def test_login_password_recovery_form(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(self.MAIN_PAGE_URL + "forgot-password")
        driver.find_element(*Locators.login_link).click()
        driver.find_element(*Locators.email_input).send_keys(self.EMAIL)
        driver.find_element(*Locators.password_input).send_keys(self.PASSWORD)
        driver.find_element(*Locators.submit_button).click()
        wait.until(EC.url_to_be(self.MAIN_PAGE_URL))
        assert driver.current_url == self.MAIN_PAGE_URL
