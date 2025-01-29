from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a")


class LoginPageLocators():
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTER_EMAIL =  (By.NAME, 'registration-email')
    REGISTER_PASSWORD = (By.NAME, 'registration-password1')
    REGISTER_CONFIRM = (By.NAME, 'registration-password2')

    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PASSWORD = (By.NAME, 'login-password')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-primary.btn-add-to-basket')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    ALERT_INFO = (By.CSS_SELECTOR, '.alert-info .alertinner strong')

    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > div.basket-title.hidden-xs')