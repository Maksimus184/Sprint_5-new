import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import Credentials
from locators import TestRegistrationLocators


main_site = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture
def start_from_main_page(driver):
    driver.get(main_site)
    return driver



