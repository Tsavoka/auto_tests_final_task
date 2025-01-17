from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        to_basket.click()

    def should_be_info_alert(self):
        self.should_be_alert_success()
        self.should_be_alert_info()

    def should_be_alert_success():
        # проверка, что правильная книга добавлена
        pass

    def should_be_alert_info():
        # проверка итоговой стоимости корзины
        pass