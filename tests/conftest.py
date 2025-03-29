import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


main_site = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture(scope="class")
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Указываем правильный путь к chromedriver
    driver_service = Service('/opt/homebrew/bin/chromedriver')
    driver = webdriver.Chrome(service=driver_service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def start_from_main_page(driver):
    driver.get(main_site)
    driver.fullscreen_window()
    yield driver