from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not in url"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "There is not login form"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "There is not register form"

    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        register_email = self.browser.find_element(*ProductPageLocators.REGISTRATION_EMAIL).send_keys(email)
        register_password_1 = self.browser.find_element(*ProductPageLocators.REGISTRATION_PASSWORD_1).send_keys(password)
        register_password_2 = self.browser.find_element(*ProductPageLocators.REGISTRATION_PASSWORD_2).send_keys(password)
        registration_submit = self.browser.find_element(*ProductPageLocators.REGISTRATION_SUBMIT).click()