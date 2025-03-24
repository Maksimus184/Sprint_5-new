from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestRegistrationLocators



def test_failed_registration(start_from_main_page):
    driver = start_from_main_page
    driver.get("https://stellarburgers.nomoreparties.site")

    # Явное ожидание (инициализация wait) перед взаимодействием с элементами
    wait = WebDriverWait(driver, 30)

    # Начинаем процесс регистрации
    driver.find_element(*TestRegistrationLocators.personal_account_button).click()
    driver.find_element(*TestRegistrationLocators.autorization_form_page).click()

    # Ждем, пока поле для имейл, пароля и имени станет видимым перед вводом данных
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.name_input)).send_keys('Maksim')
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.email_input)).send_keys('CMaksim_Maksimov_17_1984@mail.ru')
    wait.until(EC.visibility_of_element_located(TestRegistrationLocators.password_input)).send_keys('0105')

    # Явное ожидание для кнопки регистрации
    registration_button_element = wait.until(EC.element_to_be_clickable(TestRegistrationLocators.registration_button))
    registration_button_element.click()

    # Ожидание появления сообщения об ошибке
    reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestRegistrationLocators.incorrect_password_input)).text
    assert reg_text == 'Некорректный пароль'