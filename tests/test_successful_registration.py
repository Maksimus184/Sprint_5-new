from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestRegistrationLocators
from curl import URL
from data import Credentials


def test_successful_registration(start_from_main_page):
    driver = start_from_main_page
    driver.get("https://stellarburgers.nomoreparties.site")

    # Явное ожидание (инициализация wait) перед взаимодействием с элементами
    wait = WebDriverWait(driver, 30)

    # Начинаем процесс регистрации
    driver.find_element(*TestRegistrationLocators.personal_account_button).click()
    driver.find_element(*TestRegistrationLocators.autorization_form_page).click()

    # Ждем, пока поле для имейл, пароля и имени станет видимым перед вводом данных
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.name_input)).send_keys(Credentials.name)
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.email_input)).send_keys(Credentials.email)
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.password_input)).send_keys(Credentials.password)

    # Явное ожидание для кнопки регистрации
    registration_button_element = wait.until(EC.element_to_be_clickable(TestRegistrationLocators.registration_button))
    registration_button_element.click()

    # Явное ожидание для полей входа
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.email_intrance)).send_keys(
        "Maksimmaksimov_171100@mail.ru")
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.password_intrance)).send_keys("0105330")

    # Явное ожидание для кнопки входа
    log_in_button_element = wait.until(EC.element_to_be_clickable(TestRegistrationLocators.log_in_button))
    log_in_button_element.click()

    # Явное ожидание для полей входа
    wait = WebDriverWait(driver, 30)
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.email_intrance)).send_keys("Maksimmaksimov_17166@mail.ru")
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.password_intrance)).send_keys("0105329")

    # Явное ожидание для кнопки входа
    wait = WebDriverWait(driver, 30)
    log_in_button_element = wait.until(EC.element_to_be_clickable(TestRegistrationLocators.log_in_button))
    log_in_button_element.click()
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.personal_account_button))
    # Дополнительно проверяем текущий URL
    current_url = driver.current_urlwait = WebDriverWait(driver, 30)
    print(f"Current URL after login: {current_url}")
    wait.until(EC.url_to_be(URL))
    assert driver.current_url == URL
