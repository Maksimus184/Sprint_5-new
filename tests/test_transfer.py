from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestRegistrationLocators, TestLogInLocators
from curl import URL
from data import Credentials

class TestTransfer:

    def test_transfer_to_your_personal_account(self, driver):
        driver = driver
        driver.get(URL)

        # Явное ожидание (инициализация wait) перед взаимодействием с элементами
        wait = WebDriverWait(driver, 30)

        # Поиск кнопки Личного кабинета
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждем, пока поле для имейла и пароля станет видимым перед вводом данных
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.EMAIL_INPUT)).send_keys(Credentials.EMAIL)
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.PASSWORD_INPUT)).send_keys(Credentials.PASSWORD)

        # Явное ожидание для кнопки Входа
        LOG_IN_BUTTON_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.LOG_IN_BUTTON))
        LOG_IN_BUTTON_element.click()

        # Явное ожидание для кнопки Конструктор
        DESIGNER_BUTTON_LINK_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.DESIGNER_BUTTON_LINK))
        DESIGNER_BUTTON_LINK_element.click()



        wait.until(EC.url_to_be(URL))
        assert driver.current_url == URL

    def test_transfer_from_personal_account_to_logo(self, driver):
        driver = driver
        driver.get(URL)

        # Явное ожидание (инициализация wait) перед взаимодействием с элементами
        wait = WebDriverWait(driver, 30)

        # Вход в личный кабинет
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждем, пока поле для имейла и пароля станет видимым перед вводом данных
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.EMAIL_INPUT)).send_keys(Credentials.EMAIL)
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.PASSWORD_INPUT)).send_keys(Credentials.PASSWORD)

        # Явное ожидание для кнопки Входа
        LOG_IN_BUTTON_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.LOG_IN_BUTTON))
        LOG_IN_BUTTON_element.click()

        # Явное ожидание для кнопки Конструктор
        DESIGNER_BUTTON_LINK_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.DESIGNER_BUTTON_LINK))
        DESIGNER_BUTTON_LINK_element.click()

        # Переход обратно в личный кабинет
        wait.until(EC.element_to_be_clickable(TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(TestLogInLocators.DESIGNER_BUTTON_LINK)).click()

        # Переход на логотип
        wait.until(EC.element_to_be_clickable(TestLogInLocators.LOGO_BUTTON)).click()

        wait.until(EC.url_to_be(URL))
        assert driver.current_url == URL

    def test_transfer_to_your_personal_account(self, driver):
        driver = driver
        driver.get(URL)

        # Явное ожидание (инициализация wait) перед взаимодействием с элементами
        wait = WebDriverWait(driver, 30)

        # Начинаем процесс входа в личный кабинет
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждем, пока поле для имейла и пароля станет видимым перед вводом данных
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.EMAIL_INPUT)).send_keys(Credentials.EMAIL)
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.PASSWORD_INPUT)).send_keys(Credentials.PASSWORD)

        # Явное ожидание для кнопки Входа
        LOG_IN_BUTTON_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.LOG_IN_BUTTON))
        LOG_IN_BUTTON_element.click()

        wait.until(EC.url_to_be(URL))
        assert driver.current_url == URL




