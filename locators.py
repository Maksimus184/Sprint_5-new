from selenium.webdriver.common.by import By

class TestRegistrationLocators:

    PERSONAL_ACCOUNT_BUTTON = By.LINK_TEXT, "Личный Кабинет"
    AUTORIZATION_FORM_PAGE = By.CLASS_NAME, "Auth_link__1fOlj"
    NAME_INPUT = By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']"
    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    PASSWORD_INPUT = By.XPATH,  "//label[text()='Пароль']/following-sibling::input[@name='Пароль']"
    REGISTRATION_BUTTON = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]"
    LOG_IN_BUTTON = By.XPATH, "//button[contains(text(),'Войти')]"
    INCORREСT_PASSWORD_INPUT = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")
    EMAIL_LOG_IN = (By.XPATH,"//input[@name='name']")
    PASSWORD_LOG_IN = (By.XPATH,"//input[@name='Пароль']")
    IN_REG_BUTTON = (By.XPATH,"//a[@href='/login']")
    OUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
class TestLogInLocators:
    LOG_IN_BUTTON = By.XPATH, "//button[contains(@class, 'button_button__33qZ0')]"
    LOGO_BUTTON = By.CLASS_NAME, "AppHeader_header__logo__2D0X2"
    ENTER_BUTTON = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    AUTORIZATION_EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']"
    AUTORIZATION_PASSWORD = By.CSS_SELECTOR, "input[name='Пароль']"
    AUTORIZATION_NAME  = (By.XPATH, "//input[@name='name']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")
    DESIGNER_BUTTON_LINK = By.LINK_TEXT, "Конструктор"
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    RECOVERY_PASSWORD_FINISH_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    LOG_IN_EMAIL = (By.XPATH, "//input[@name='name']")
    LOG_IN_PASSWORD = (By.XPATH, "//input[@name='Пароль' and @type='password']")
class LocatorsBurgerConstructorLocators:
    BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Булки')]")
    SAUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Соусы')]")
    FILLINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Начинки')]")
    NAME_BUTTON_SECTION_BUNS = (By.XPATH, "//span[text() = 'Булки']")
    NAME_BUTTON_SECTION_SAUCES = (By.XPATH, "//span[text() = 'Соусы']")
    NAME_BUTTON_SECTION_FILLINGS = (By.XPATH, "//span[text() = 'Начинки']")
    TAB_SELECTED = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")