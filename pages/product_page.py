from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_add_basket(self):
        add_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_basket_button.click()

    def should_be_product_in_basket(self):
        product_added_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_BASKET).text
        product_name =  self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_added_basket == product_name, "Product is not in basket"

    def should_be_price_in_basket(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert price_basket ==  product_price, "Don't have price in basket"
