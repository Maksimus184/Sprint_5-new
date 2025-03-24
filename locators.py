from selenium.webdriver.common.by import By


class TestRegistrationLocators:
    personal_account_button = By.LINK_TEXT, "Личный Кабинет"
    autorization_form_page = By.CLASS_NAME, "Auth_link__1fOlj"
    name_input = By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']"
    email_input = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    password_input = By.XPATH,  "//label[text()='Пароль']/following-sibling::input[@name='Пароль']"
    registration_button = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"
    incorrect_password_input = (By.XPATH, "//p[@class = 'input__error text_type_main-default']")
    email_intrance = (By.XPATH, "//input[@type='text' and @name='name']")
    password_intrance = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    log_in_button = By.XPATH, "//button[contains(text(),'Войти')]"
    incorrect_password_input = (By.XPATH, "//p[@class = 'input__error text_type_main-default']")

class TestLogInLocators:
    log_in_button = By.XPATH, "//button[contains(text(),'Войти')]"
    logo_button = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
    enter_button = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    autorization_email = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    autorization_password = By.CSS_SELECTOR, "input[name='Пароль']"
    sign_in_button = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")
    place_an_order_button = By.XPATH, "//button[contains(text(), 'Оформить заказ')]"
    designer_button_link = By.LINK_TEXT, "Конструктор"
    logo_link = (By.XPATH, "//div/a[@href = '/']")
    log_in_title = (By.XPATH, "//h2[text() = 'Вход']")
    personal_account_button = (By.XPATH, "//p[text() = 'Личный Кабинет']")
    make_a_burger = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    profile_link = (By.XPATH, "//a[@href='/account/profile']")
    log_out_button = (By.XPATH, "//button[contains(text(), 'Выход')]")
    recovery_password_button = (By.XPATH, "//a[text()='Восстановить пароль']")
    recovery_password_finish_button = (By.XPATH, "//button[text()='Восстановить']")
class LocatorsBurgerConstructorLocators:
    BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Булки')]")
    SAUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Соусы')]")
    FILLINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Начинки')]")
    NAME_BUTTON_SECTION_BUNS = (By.XPATH, "//span[text() = 'Булки']")
    NAME_BUTTON_SECTION_SAUCES = (By.XPATH, "//span[text() = 'Соусы']")
    NAME_BUTTON_SECTION_FILLINGS = (By.XPATH, "//span[text() = 'Начинки']")
    buns_section = (By.XPATH, "//h2[text() = 'Булки']")
    sauces_section = (By.XPATH, "//h2[text() = 'Соусы']")
    fillings_section = (By.XPATH, "//h2[text() = 'Начинки']")
    personal_account_button = (By.XPATH, "//p[text() = 'Личный Кабинет']")
    log_in_account_button = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    tab_selected = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")