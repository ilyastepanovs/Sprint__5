import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import PROFILE_URL
from locators import Locators


@pytest.mark.usefixtures("driver", "login")
class TestProfileTransition:

    def test_transition_personal_account(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.profile_button).click()
        wait.until(EC.url_to_be(PROFILE_URL))
        assert driver.current_url == PROFILE_URL

