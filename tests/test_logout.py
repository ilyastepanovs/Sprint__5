import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.mark.usefixtures("driver", "login")
class TestLogout:
    LOGIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/login"

    def test_go_to_constructor_by_logo(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.profile_button).click()

        exit_button = wait.until(EC.visibility_of_element_located(Locators.exit_button))
        exit_button.click()

        wait.until(EC.url_to_be(self.LOGIN_PAGE_URL))
        assert driver.current_url == self.LOGIN_PAGE_URL
