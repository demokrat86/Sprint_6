import allure

from urls import Urls
from pages.main_page import MainPage


class TestLogo:

    @allure.title('Проверка перехода на главную страницу Самоката по клику на лого "Самокат"')
    def test_scooter_logo_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookie_btn()
        main_page.click_order_button()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        title_is_displayed = main_page.check_order_title_displaying()
        assert current_url == Urls.QA_SCOOTER_URL and title_is_displayed

    @allure.title('Проверка редиректа на страницу Дзен по клику на лого "Яндекс"')
    def test_yandex_logo_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_accept_cookie_btn()
        main_page.click_yandex_logo()
        main_page.go_to_new_tab()
        main_page.check_element_main_button()
        current_url = main_page.get_current_url()
        assert current_url == Urls.DZEN_URL
