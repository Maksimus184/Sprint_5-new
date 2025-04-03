from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLogInLocators, TestRegistrationLocators
from curl import URL, RESET_PASSWORD_URL
from data import Credentials

class TestEntrance:

    def test_successful_entrance_from_main_page(self, driver):
        driver = driver
        driver.get(URL)

        wait = WebDriverWait(driver, 30)

        # Начинаем процесс входа
        wait.until(EC.element_to_be_clickable(TestLogInLocators.ENTER_BUTTON)).click()

        # Вводим данные для логина
        wait.until(EC.visibility_of_element_located(TestLogInLocators.LOG_IN_EMAIL)).send_keys(Credentials.EMAIL)
        wait.until(EC.visibility_of_element_located(TestLogInLocators.LOG_IN_PASSWORD)).send_keys(Credentials.PASSWORD)

        # Кликаем по кнопке логина
        LOG_IN_BUTTON_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.LOG_IN_BUTTON))
        LOG_IN_BUTTON_element.click()

        # Ждем, пока URL изменится
        wait = WebDriverWait(driver, 30)
        wait.until(EC.url_to_be(URL))
        assert driver.current_url == URL

    def test_entrance_from_password_recovery_page(self, driver):
        driver = driver
        driver.get(URL)

        # Явное ожидание (инициализация wait) перед взаимодействием с элементами
        wait = WebDriverWait(driver, 30)

        # Начинаем процесс восстановления пароля
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLogInLocators.RECOVERY_PASSWORD_BUTTON).click()

        # Ждем, пока поле для имени станет видимым перед вводом данных
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.EMAIL_INPUT)).send_keys(Credentials.EMAIL)

        # Явное ожидание для кнопки Восстановить
        RECOVERY_PASSWORD_FINISH_BUTTON_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.RECOVERY_PASSWORD_FINISH_BUTTON))
        RECOVERY_PASSWORD_FINISH_BUTTON_element.click()

        # Ожидание изменения URL и проверка на соответствие
        wait.until(EC.url_to_be(RESET_PASSWORD_URL))
        assert driver.current_url == RESET_PASSWORD_URL

    def test_successful_entrance_from_personal_account(self, driver):
        driver = driver
        driver.get(URL)

        # Явное ожидание (инициализация wait) перед взаимодействием с элементами
        wait = WebDriverWait(driver, 30)

        # Начинаем процесс входа по кнопке Войти на главной странице
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждем, пока поле для имени и пароля станет видимым перед вводом данных
        wait.until(EC.visibility_of_element_located(TestLogInLocators.AUTORIZATION_EMAIL)).send_keys(Credentials.EMAIL)
        wait.until(EC.visibility_of_element_located(TestLogInLocators.AUTORIZATION_PASSWORD)).send_keys(
            Credentials.PASSWORD)

        # Явное ожидание для кнопки Входа
        LOG_IN_BUTTON_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.LOG_IN_BUTTON))
        LOG_IN_BUTTON_element.click()

        # Ждем, пока URL изменится на ожидаемый
        wait.until(EC.url_to_be(URL))
        assert driver.current_url == URL

    def test_successful_entrance_from_personal_account(self, driver):
        driver = driver
        driver.get(URL)

        # Явное ожидание (инициализация wait) перед взаимодействием с элементами
        wait = WebDriverWait(driver, 30)

        # Начинаем процесс входа по кнопке Войти на главной странице
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждем, пока поле для имени и пароля станет видимым перед вводом данных
        wait.until(EC.visibility_of_element_located(TestLogInLocators.AUTORIZATION_EMAIL)).send_keys(Credentials.EMAIL)
        wait.until(EC.visibility_of_element_located(TestLogInLocators.AUTORIZATION_PASSWORD)).send_keys(
            Credentials.PASSWORD)

        # Явное ожидание для кнопки Входа
        LOG_IN_BUTTON_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.LOG_IN_BUTTON))
        LOG_IN_BUTTON_element.click()

        # Ждем, пока URL изменится на ожидаемый
        wait.until(EC.url_to_be(URL))
        assert driver.current_url == URL
