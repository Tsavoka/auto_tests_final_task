from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        # Добавление элемента в корзину.  
        to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        to_basket.click()

    def should_be_info_alert(self):
        self.should_be_currect_book()
        self.should_be_currect_price()

    def should_be_currect_book(self):
        # Проверка, что правильная книга добавлена.  
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS).text
        assert book_name == alert_book_name, f'{book_name} is not alert {alert_book_name}'

    def should_be_currect_price(self):
        # Проверка итоговой стоимости корзины.  
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        alert_book_price = self.browser.find_element(*ProductPageLocators.ALERT_INFO).text
        assert book_price == alert_book_price, f'{book_price} is not alert {alert_book_price}'

    def should_not_be_success_message(self):
        # Проверка, что сообщения об успехе нет.  
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
        "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        # Проверка, что сообщения об успехе исчезло.  
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
        "Success message have not disappeared, as it should be"