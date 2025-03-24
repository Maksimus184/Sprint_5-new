from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestRegistrationLocators, TestLogInLocators
from curl import URL
from data import Credentials


def test_transfer_to_your_personal_account(start_from_main_page):
    driver = start_from_main_page
    driver.get("https://stellarburgers.nomoreparties.site")

    # Явное ожидание (инициализация wait) перед взаимодействием с элементами
    wait = WebDriverWait(driver, 30)

    # Поиск кнопки Личного кабинета
    driver.find_element(*TestRegistrationLocators.personal_account_button).click()

    # Ждем, пока поле для пароля и имейл станет видимым перед вводом данных
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.email_input)).send_keys(Credentials.email)
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.password_input)).send_keys(Credentials.email)
    # Явное ожидание для кнопки Входа
    log_in_button_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.log_in_button))
    log_in_button_element.click()
    constructor_button_link_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.constructor_button_link))
    constructor_button_link_element.click()
    driver.find_element(*TestRegistrationLocators.personal_account_button).click()
    driver.find_element(*TestLogInLocators.designer_button_link).click()
    # Дополнительно проверяем текущий URL
    current_url = driver.current_urlwait = WebDriverWait(driver, 30)
    print(f"Current URL after login: {current_url}")
    wait.until(EC.url_to_be(URL))
    assert driver.current_url == URL




