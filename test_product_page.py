import time
import pytest

from pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_message_product_has_been_added_to_basket()
    page.check_message_cost_of_the_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    # Открываем страницу товара
    page.open()
    # Добавляем товар в корзину
    page.add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    # Открываем страницу товара
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    # Открываем страницу товара
    page.open()
    # Добавляем товар в корзину
    page.add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_be_disappeared_success_message()
