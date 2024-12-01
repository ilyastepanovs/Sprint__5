import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.mark.usefixtures("driver")
class TestSignUp:
    LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"

    def test_successful_registration(self, driver, registration_data, valid_random_pass):
        name, email = registration_data
        password = valid_random_pass
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.registration_link).click()
        driver.find_element(*Locators.name_input).send_keys(name)
        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.register_button).click()
        wait.until(EC.url_to_be(self.LOGIN_PAGE_URL))
        assert driver.current_url == self.LOGIN_PAGE_URL

    def test_unsuccessful_registration(self, driver, registration_data, invalid_random_pass):
        name, email = registration_data
        password = invalid_random_pass
        driver.find_element(*Locators.login_button).click()
        driver.find_element(*Locators.registration_link).click()
        driver.find_element(*Locators.name_input).send_keys(name)
        driver.find_element(*Locators.email_input).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.register_button).click()
        error_text = driver.find_element(*Locators.invalid_password_error).text
        assert error_text == "Некорректный пароль"

