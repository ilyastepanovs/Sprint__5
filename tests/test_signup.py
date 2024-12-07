import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import LOGIN_PAGE_URL
from locators import Locators
from data_helper import NAME, get_random_email, get_random_password


@pytest.mark.usefixtures("driver")
class TestSignUp:

    def test_successful_registration(self, driver):
        name = NAME
        email = get_random_email()
        password = get_random_password()
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.registration_link).click()
        driver.find_element(*Locators.name_input).send_keys(name)
        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.register_button).click()
        wait.until(EC.url_to_be(LOGIN_PAGE_URL))
        assert driver.current_url == LOGIN_PAGE_URL

    def test_unsuccessful_registration(self, driver):
        name = NAME
        email = get_random_email()
        password = get_random_password(False)
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.registration_link).click()
        driver.find_element(*Locators.name_input).send_keys(name)
        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.register_button).click()
        error_text = driver.find_element(*Locators.invalid_password_error).text
        assert error_text == "Некорректный пароль"

