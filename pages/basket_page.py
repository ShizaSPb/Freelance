from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert not self.is_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Basket is not empty, but should be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE), "Message about empty basket is not presented, but should be"
