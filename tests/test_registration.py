import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestRegistrationLocators, TestLogInLocators
from curl import URL, LOGIN_URL
from data import Credentials


class TestRegistration:
    def test_successful_registration(self, driver):
        driver = driver
        driver.get(URL)

        wait = WebDriverWait(driver, 60)

    # Начинаем процесс регистрации
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestRegistrationLocators.AUTORIZATION_FORM_PAGE).click()

        unique_email = str(uuid.uuid4()) + "@example.com"
        print(f"Generated Email: {unique_email}")

        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.NAME_INPUT)).send_keys(Credentials.NAME)
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.EMAIL_INPUT)).send_keys(unique_email)
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.PASSWORD_INPUT)).send_keys(Credentials.PASSWORD)

        REGISTRATION_BUTTON_element = wait.until(EC.element_to_be_clickable(TestRegistrationLocators.REGISTRATION_BUTTON))
        REGISTRATION_BUTTON_element.click()

        # Проверяем, что после входа мы находимся на правильной странице
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_failed_registration(self, driver):
        driver = driver
        driver.get(URL)

        # Явное ожидание (инициализация wait) перед взаимодействием с элементами
        wait = WebDriverWait(driver, 30)

        # Начинаем процесс регистрации
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestRegistrationLocators.AUTORIZATION_FORM_PAGE).click()

        # Ждем, пока поле для имени, имейл и пароля станут видимыми перед вводом данных
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.NAME_INPUT)).send_keys('Maksim')
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.EMAIL_INPUT)).send_keys(
            'CMaksim_Maksimov_17_1984@mail.ru')
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.PASSWORD_INPUT)).send_keys('0105')

        # Явное ожидание для кнопки регистрации
        REGISTRATION_BUTTON_element = wait.until(
            EC.element_to_be_clickable(TestRegistrationLocators.REGISTRATION_BUTTON))
        REGISTRATION_BUTTON_element.click()

        # Ожидание появления сообщения об ошибке
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestRegistrationLocators.INCORREСT_PASSWORD_INPUT)).text
        assert reg_text == 'Некорректный пароль'