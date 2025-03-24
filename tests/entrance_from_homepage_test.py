from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestRegistrationLocators,TestLogInLocators
from curl import URL
from data import Credentials


def test_successful_entrance_from_main_page(start_from_main_page):
    driver = start_from_main_page
    driver.get("https://stellarburgers.nomoreparties.site")

    # Явное ожидание (инициализация wait) перед взаимодействием с элементами
    wait = WebDriverWait(driver, 30)

    # Начинаем процесс входа по кнопке Войти на главной странице
    driver.find_element(*TestRegistrationLocators.enter_button).click()
    driver.find_element(*TestRegistrationLocators.autorization_form_page).click()

    # Ждем, пока поле для имени и пароля станет видимым перед вводом данных
    wait.until(EC.visibility_of_element_located(TestLogInLocators.autorization_email)).send_keys(Credentials.email)
    wait.until(EC.visibility_of_element_located(TestLogInLocators.autorization_password)).send_keys(Credentials.password)

    # Явное ожидание для кнопки входа
    log_in_button_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.log_in_button))
    log_in_button_element.click()

    # Дополнительно проверяем текущий URL
    current_url = driver.current_urlwait = WebDriverWait(driver, 30)
    print(f"Current URL after login: {current_url}")
    wait.until(EC.url_to_be(URL))
    assert driver.current_url == URL
