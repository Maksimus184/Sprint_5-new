from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestRegistrationLocators, TestLogInLocators
from curl import LOGIN_URL, URL
from data import Credentials


class TestUserAccount:

    def test_transfer_to_your_personal_account(self, driver):
        driver = driver
        driver.get(URL)

        # Явное ожидание (инициализация wait) перед взаимодействием с элементами
        wait = WebDriverWait(driver, 30)

        # Поиск кнопки Личного кабинета
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Ждем, пока поле для емайл и пароля станет видимым перед вводом данных
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.EMAIL_INPUT)).send_keys(Credentials.EMAIL)
        wait.until(EC.visibility_of_element_located(TestRegistrationLocators.PASSWORD_INPUT)).send_keys(Credentials.PASSWORD)

        # Явное ожидание для кнопки Входа
        LOG_IN_BUTTON_element = wait.until(EC.element_to_be_clickable(TestLogInLocators.LOG_IN_BUTTON))
        LOG_IN_BUTTON_element.click()

        # Поиск кнопки Личного кабинета
        driver.find_element(*TestRegistrationLocators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(EC.element_to_be_clickable(TestRegistrationLocators.OUT_BUTTON)).click()

        # Ждем, пока URL изменится на ожидаемый
        wait.until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL



