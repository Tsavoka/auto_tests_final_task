from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_basket_url()
        self.should_be_empty()
        self.should_not_be_something()

    def should_be_basket_url(self):
        # Проверка на корректный url адрес.  
        assert "basket" in self.browser.current_url, "This is not a basket page"

    def should_be_empty(self):
        # Корзина должна быть пуста.  
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
        "Basket not empty, but it should be"

    def should_not_be_something(self):
        # В корзине не должно что-либо быть.  
        assert self.is_not_element_present(*BasketPageLocators.NOT_EMPTY_BASKET), \
        "Something in basket, but it should't be"