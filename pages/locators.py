from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) strong')
    MESSAGE_ITEM_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) strong')

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, '.basket_summary')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')