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
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS).text
        assert book_name == alert_book_name, f'{book_name} is not alert {alert_book_name}'

    def should_be_currect_price(self):
        # проверка итоговой стоимости корзины
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        alert_book_price = self.browser.find_element(*ProductPageLocators.ALERT_INFO).text
        assert book_price == alert_book_price, f'{book_price} is not alert {alert_book_price}'