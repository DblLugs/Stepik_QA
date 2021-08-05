from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_button(self):
        self.browser.find_element(*BasketPageLocators.BASKET_BUTTON).click()

    def basket_is_not_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_BASKET), "Basket has item"

    def should_be_message_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET), "Basket has item"
