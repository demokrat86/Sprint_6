import allure
import pytest

from data import Users
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Оформление заказа через 2 разных точки входа')
    @pytest.mark.parametrize('button, user', [[MainPageLocators.order_btn_top, Users.user1],
                                              [MainPageLocators.order_button_low, Users.user2]])
    def test_order_scooter(self, driver, button, user):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_accept_cookie_btn()
        main_page.scroll_to_element(button)
        main_page.click_button(button)
        order_page.filling_first_order_form(user)
        order_page.filling_second_order_form(user)
        order_page.click_yes_order_scooter()
        assert order_page.check_order_title()
