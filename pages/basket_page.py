from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket selector not found"
        test_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert test_text == "Your basket is empty. Continue shopping", "Empty basket text not found"

    def is_no_item_to_buy(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_TEXT),\
            "There is \"items to buy\" table, but should not be"