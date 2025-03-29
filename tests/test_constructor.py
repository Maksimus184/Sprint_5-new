from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsBurgerConstructorLocators
from curl import URL


class TestBurgerConstructor:

    def test_designer_check_tabs_sauces_button(self, start_from_main_page):
        driver = start_from_main_page
        driver.get(URL)

        driver.find_element(*LocatorsBurgerConstructorLocators.SAUCES_BUTTON).click()

        # Используем TAB_SELECTED для проверки активности таба
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LocatorsBurgerConstructorLocators.TAB_SELECTED))
        current_class = driver.find_element(*LocatorsBurgerConstructorLocators.TAB_SELECTED).get_attribute('class')
        assert "tab_tab_type_current" in current_class

    def test_designer_check_tabs_fillings_button(self, start_from_main_page):
        driver = start_from_main_page
        driver.get(URL)

        driver.find_element(*LocatorsBurgerConstructorLocators.FILLINGS_BUTTON).click()

        # Используем TAB_SELECTED для проверки активности таба
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LocatorsBurgerConstructorLocators.TAB_SELECTED))
        current_class = driver.find_element(*LocatorsBurgerConstructorLocators.TAB_SELECTED).get_attribute('class')
        assert "tab_tab_type_current" in current_class

    def test_designer_check_tabs_filling_rolls(self, start_from_main_page):
        driver = start_from_main_page
        driver.get(URL)

        driver.find_element(*LocatorsBurgerConstructorLocators.FILLINGS_BUTTON).click()
        driver.find_element(*LocatorsBurgerConstructorLocators.BUNS_BUTTON).click()

        # Используем TAB_SELECTED для проверки активности таба
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LocatorsBurgerConstructorLocators.TAB_SELECTED))
        current_class = driver.find_element(*LocatorsBurgerConstructorLocators.TAB_SELECTED).get_attribute('class')
        assert "tab_tab_type_current" in current_class