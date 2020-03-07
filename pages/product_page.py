from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        btn = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        btn.click()

    def get_product_title(self):
        element = self.browser.find_element(
            *ProductPageLocators.PRODUCT_TITLE)
        return element.text

    def get_product_price(self):
        element = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        return element.text

    def get_message_product_title(self):
        element = self.browser.find_element(
            *ProductPageLocators.MESSAGE_PRODUCT_TITLE)
        return element.text

    def get_message_cost_basket(self):
        element = self.browser.find_element(
            *ProductPageLocators.MESSAGE_COST_BASKET)
        return element.text

    def check_message_product_has_been_added_to_basket(self):
        title = self.get_product_title()
        title_from_message = self.get_message_product_title()
        assert title == title_from_message, \
            f'Expected "{title}", but "{title_from_message}" was received'

    def check_message_cost_of_the_basket(self):
        price = self.get_product_price()
        cost_basket_from_message = self.get_message_cost_basket()
        assert price == cost_basket_from_message, f'Expected "{price}", but "{cost_basket_from_message}" was received'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should was"
