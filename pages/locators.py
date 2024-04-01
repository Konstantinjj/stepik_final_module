from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
