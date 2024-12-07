import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.mark.usefixtures("driver")
class TestTabs:

    def is_tab_active(self, driver, locator):
        tab_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return "tab_tab_type_current__2BEPc" in tab_element.get_attribute("class")

    def test_constructor_sauce(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.sauces_tab).click()
        assert self.is_tab_active(driver, Locators.sauces_tab_div)

    def test_constructor_buns(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.sauces_tab).click()
        driver.find_element(*Locators.buns_tab).click()
        assert self.is_tab_active(driver, Locators.buns_tab_div)

    def test_constructor_filling(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.find_element(*Locators.filling_tab).click()
        assert self.is_tab_active(driver, Locators.filling_tab_div)
