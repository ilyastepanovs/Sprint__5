import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.mark.usefixtures("driver", "login")
class TestProfileTransition:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    PROFILE_URL = BASE_URL + "/account/profile"
    EMAIL = "ilyastepanov131989@yandex.ru"
    PASSWORD = "123456"

    def test_transition_personal_account(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.profile_button).click()
        wait.until(EC.url_to_be(self.PROFILE_URL))
        assert driver.current_url == self.PROFILE_URL

