from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def should_be_add_product_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_product_to_basket(self):
        self.should_be_add_product_button()
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_name_in_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME_ADDED), "Product name is not presented in basket"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def should_be_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "Basket price is not presented"

    def get_product_name(self):
        self.should_be_product_name()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_basket_name(self):
        self.should_be_product_name_in_basket()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED).text

    def get_product_price(self):
        self.should_be_product_price()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_basket_price(self):
        self.should_be_basket_price()
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def check_added_product(self):
        product_name = self.get_product_name()
        product_basket_name = self.get_product_basket_name()
        product_price = self.get_product_price()
        product_basket_price = self.get_product_basket_price()
        assert product_name == product_basket_name, "Product name difference"
        assert product_price == product_basket_price, "Product price difference"

