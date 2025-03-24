from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LocatorsBurgerConstructorLocators


def test_designer_check_tabs_sauses_button(start_from_main_page):
    driver = start_from_main_page
    driver.get("https://stellarburgers.nomoreparties.site")


    driver.find_element(*LocatorsBurgerConstructorLocators.SAUCES_BUTTON).click()
    current_class = driver.find_element(*LocatorsBurgerConstructorLocators.SAUCES_BUTTON).get_attribute('class')
    assert "tab_tab_type_current" in current_class


def test_designer_check_tabs_fillings_button(start_from_main_page):
    driver = start_from_main_page
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*LocatorsBurgerConstructorLocators.FILLINGS_BUTTON).click()
    current_class = driver.find_element(*LocatorsBurgerConstructorLocators.FILLINGS_BUTTON).get_attribute('class')
    assert "tab_tab_type_current" in current_class

def test_designer_check_tabs_filling_rolls(start_from_main_page):
    driver = start_from_main_page
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*LocatorsBurgerConstructorLocators.FILLINGS_BUTTON).click()
    driver.find_element(*LocatorsBurgerConstructorLocators.BUNS_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LocatorsBurgerConstructorLocators.tab_selected)
    )
    current_class = driver.find_element(*LocatorsBurgerConstructorLocators.BUNS_BUTTON).get_attribute('class')
    assert "tab_tab_type_current" in current_class