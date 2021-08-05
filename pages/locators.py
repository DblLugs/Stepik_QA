from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "span>a.btn.btn-default")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCT_BASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_ADDED_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    LOGIN_LINK = (By.CSS_SELECTOR, "a#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

