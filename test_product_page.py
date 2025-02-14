import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import LINK_PRODUCT


link = LINK_PRODUCT

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [pytest.param("7", marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # Гость может добавить товар в корзину.  
    link = f"{link}?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_info_alert()
    page.success_message_should_disappear()
 

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # После добавления в корзину нет сообщения об успехе.  
    # Ожидаемое падение: сообщение об успехе должно быть.  
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # На любой странице нет сообщений об успехе.  
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # Сообщение о добавлении в корзину должно исчезать.  
    # Ожидаемое падение: на сайте не пропадают эти сообщения.  
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    # На любой странице есть кнопка логина.  
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page(browser):
    # Гость может перейти с любой станицы на страницу логина.  
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Переходя с любой страницы на страницу корзины, гость видит пустую 
    # корзину.  
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Манипулировать браузером в сетапе и уж тем более что-то там 
        # проверять — это плохая практика, лучше так не делать без 
        # особой необходимости. Здесь этот пример исключительно в 
        # учебных целях, чтобы вы попробовали писать сетапы для тестов. 
        # В реальной жизни мы реализовали бы все эти манипуляции с 
        # помощью API или напрямую через базу данных.  
        #
        # Этот сетап переходит с любой страницы на страницу логина, и 
        # регистрирует там нового пользователя.  
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # На любой странице нет сообщений об успехе.  
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Зарегистрированный пользователь может добавить товар в корзину.  
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_to_basket()
        page.should_be_info_alert()


'''
# Выше этот тест вынесен с одним параметром в параметризации, чтобы не 
# ждать слишком долго.  Можно раскомментировать этот код и любоваться
# на его выполнение две минуты.  Очень красиво!  Поэтому этот код
# останется здесь, извините!  (:  

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6",
                                         pytest.param(
                                             "7", marks=pytest.mark.xfail),
                                         "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    # Гость может добавить товар в корзину.  
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    # page.should_not_be_success_message()       Метод работает, а коммент, чтобы не ждать
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_info_alert()
    # page.success_message_should_disappear()    Не должно исчезать, поэтому всегда проваливается
'''