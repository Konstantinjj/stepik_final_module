from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def test_add_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        BasePage.solve_quiz_and_get_code(self)
        self.should_be_success_message()
        self.should_be_product_added_to_basket()
        self.should_be_correct_basket_price()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET), \
            "Product in basket is not presented"
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        assert self.get_product_name() == product_in_basket.text, "Product name in message is not correct"

    def should_be_correct_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), \
            "Basket price is not presented"
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert self.get_product_price() == basket_price.text, "Product price is not equal basket price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is still present, but should disappear"
