from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        to_basket.click()

    def should_be_info_alert(self):
        self.should_be_currect_book()
        self.should_be_currect_price()

    def should_be_currect_book(self):
        # проверка, что правильная книга добавлена
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_INFO).text.split('\n')[0]
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS).text.split('\n')[1]
        assert book_name in alert_book_name, f'{book_name} is not alert {alert_book_name}'

    def should_be_currect_price(self):
        # проверка итоговой стоимости корзины
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_INFO).text.split('\n')[1]
        alert_book_price = self.browser.find_element(*ProductPageLocators.ALERT_INFO).text.split('\n')[1]
        assert book_price in alert_book_price, f'{book_price} is not alert {alert_book_price}'