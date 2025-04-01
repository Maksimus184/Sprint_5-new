import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

main_site = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture(scope="class")
def driver():
    # Инициализация драйвера
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Используем webdriver_manager для автоматической загрузки chromedriver
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=options)

    # Открываем главную страницу
    driver.get(main_site)
    driver.fullscreen_window()

    yield driver  # Возвращаем драйвер для использования в тестах

    driver.quit()  # Закрываем драйвер после завершения тестов