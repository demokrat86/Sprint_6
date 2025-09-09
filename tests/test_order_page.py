import allure

from helps.data import Users
from pages.home_page import HomePage, HomePageHeader
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Позитивный тест: заказ самоката через кнопку "Заказать" в хедере')
    @allure.description(
    '''1) На главной странице кликаем на верхнюю кнопку "Заказать" в хедере
       2) Заполняем форму "Для кого самокат" и нажимаем "Далее"
       3) Заполняем форму "Про аренду" и нажимаем "Заказать"
       4) Подтверждаем заказ и проверяем, что появилось окно "Заказ оформлен"'''
    )
    def test_order_scooter_by_order_button_from_header(self, driver):
        header = HomePageHeader(driver)
        order_page = OrderPage(driver)
        home_page = HomePage(driver)

        # Принимаем куки
        home_page.accept_cookie_home_page()

        # Переходим к заказу через хедер
        header.click_top_order_button()

        # Проходим весь путь заказа
        order_page.order_scooter_full_path(Users.USER_ANDREY)

        # Проверяем, что заказ оформлен
        assert order_page.check_order_confirmation_title(), "Окно подтверждения заказа не появилось"


    @allure.title('Позитивный тест: заказ самоката через кнопку "Заказать" на главной странице')
    @allure.description(
    '''1) На главной странице скроллим к нижней кнопке "Заказать" и кликаем
       2) Заполняем форму "Для кого самокат" и нажимаем "Далее"
       3) Заполняем форму "Про аренду" и нажимаем "Заказать"
       4) Подтверждаем заказ и проверяем, что появилось окно "Заказ оформлен"'''
    )
    def test_order_scooter_by_order_button_from_home_page(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)

        # Принимаем куки
        home_page.accept_cookie_home_page()

        # Кликаем по нижней кнопке "Заказать"
        home_page.scroll_and_click_bottom_order_button()

        # Проходим весь путь заказа
        order_page.order_scooter_full_path(Users.USER_MAXIM)

        # Проверяем, что заказ оформлен
        assert order_page.check_order_confirmation_title(), "Окно подтверждения заказа не появилось"
