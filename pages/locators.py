from selenium.webdriver.common.by import By

class HomePageLocators():
    """
    Locators used on Home Page
    """
    USER_BTN = (By. CSS_SELECTOR, "#userMenuToggle > span")
    REGISTER_BTN = (By. CSS_SELECTOR, "#userMenu > div > div > form > div.form-group.register > a")
    COOKIE_ALERT = (By.CLASS_NAME, "cc-cookie-accept")

class NewAccountPageLocators():
    """
    Locators used on New Account Page
    """
    FIRST_NAME = (By.ID, "sf_guard_user_first_name")
    LAST_NAME = (By.ID, "sf_guard_user_last_name")
    EMAIL = (By.ID, "sf_guard_user_email_address")
    SEX_FIELD = (By.ID, "sf_guard_user_sex_id")
    PASSWORD = (By.ID, "sf_guard_user_password")
    REPEAT_PASSWORD = (By.ID, "sf_guard_user_password_again")
    FIRST_CHECKBOX = (By.CSS_SELECTOR, "#main-scroll > div.wrapper.wrapper-js > section.container.fadeIn > article.row.logowanie > div:nth-child(2) > form > span:nth-child(11) > label > span")
    SECOND_CHECKBOX = (By.CSS_SELECTOR, "#main-scroll > div.wrapper.wrapper-js > section.container.fadeIn > article.row.logowanie > div:nth-child(2) > form > span:nth-child(12) > label > span")
    SUBMIT = (By.XPATH, "/html/body/div[1]/section[1]/article[2]/div[2]/form/button")
    ERROR_ALERT_POSITION = (By.CSS_SELECTOR, "#main-scroll > div.wrapper.wrapper-js > section.container.fadeIn > article.row.logowanie > div:nth-child(2) > form > span:nth-child(6) > span")
    ERROR_ALERT_EXPECTED = "Niepoprawny format."


class PurchasePageLocators():
    """
    Locators used on Purchase Page
    """
    WOMEN_SITE = (By.ID, "main378")
    EXAMPLE_PRODUCT = (By.CSS_SELECTOR, "#productList > div:nth-child(1) > a > span.opis > p")
    ADD_PRODUCT = (By.CLASS_NAME, "add-to-cart-btn  ")
    SHOP_INFO = (By.CSS_SELECTOR, "#cartMenuToggle > span > span")
    SHOP_INFO_EXPECTED = "1"