import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import STELLAR_BURGERS_URL
from locators import Locators


@pytest.mark.usefixtures("driver", "login")
class TestConstructorTransition:

    def test_go_to_constructor_by_logo(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.profile_button).click()
        driver.find_element(*Locators.logo).click()
        wait.until(EC.url_to_be(STELLAR_BURGERS_URL))
        assert driver.current_url == STELLAR_BURGERS_URL

    def test_go_to_constructor_by_button(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.profile_button).click()
        driver.find_element(*Locators.constructor_button).click()
        wait.until(EC.url_to_be(STELLAR_BURGERS_URL))
        assert driver.current_url == STELLAR_BURGERS_URL

