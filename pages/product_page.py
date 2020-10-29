from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_correct_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        message_name = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_NAME).text
        assert item_name == message_name, 'Item NAME does not match with the one you added'

    def should_be_correct_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_PRICE).text
        assert item_price == message_price, 'Item PRICE does not match with the one you added'

    def should_disappear_success_message_about_adding_to_cart(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ITEM_NAME), "Success message did not disappear"

    def should_not_be_success_message_about_adding_to_cart(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ITEM_NAME), "Success message is presented"