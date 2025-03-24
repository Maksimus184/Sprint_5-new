from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestRegistrationLocators, TestLogInLocators
from curl import reset_password_URL
from data import Credentials


def test_entrance_from_password_recovery_page(start_from_main_page):
    driver = start_from_main_page
    driver.get("https://stellarburgers.nomoreparties.site")

    # Явное ожидание (инициализация wait) перед взаимодействием с элементами
    wait = WebDriverWait(driver, 30)

    # Начинаем процесс восстановления пароля
    driver.find_element(*TestRegistrationLocators.personal_account_button).click()
    driver.find_element(*TestLogInLocators.recovery_password_button).click()

    # Ждем, пока поле для имени станет видимым перед вводом данных
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.email_input)).send_keys(Credentials.email)

    # Явное ожидание для кнопки Восстановить
    recovery_password_finish_button_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.recovery_password_finish_button))
    recovery_password_finish_button_element.click()

    # Дополнительно проверяем текущий URL
    current_url = driver.current_urlwait = WebDriverWait(driver, 30)
    print(f"Current URL after login: {current_url}")
    wait.until(EC.url_to_be(reset_password_URL))
    assert driver.current_url == reset_password_URL



