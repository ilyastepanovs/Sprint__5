import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


@pytest.mark.usefixtures("driver", "login")
class TestConstructorTransition:
    MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"

    def test_go_to_constructor_by_logo(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.profile_button).click()
        driver.find_element(*Locators.logo).click()
        wait.until(EC.url_to_be(self.MAIN_PAGE_URL))
        assert driver.current_url == self.MAIN_PAGE_URL

    def test_go_to_constructor_by_button(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.profile_button).click()
        driver.find_element(*Locators.constructor_button).click()
        wait.until(EC.url_to_be(self.MAIN_PAGE_URL))
        assert driver.current_url == self.MAIN_PAGE_URL

