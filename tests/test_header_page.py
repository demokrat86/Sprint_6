import pytest
import allure
from selenium.webdriver.common.by import By

from helps.data import Questions, Urls
from locators.home_page_locators import ScooterHomePageLocators, ScooterMainPageLocators
from pages.home_page import HomePage, HomePageHeader  # ✅ Обязательно добавлено!
from pages.dzen_page import DzenPage


class TestMainPage:

    @allure.title('Тест проверки перехода на главную страницу по клику на логотип "Самокат"')
    @allure.description(
        '''1) Кликаем на кнопку "Заказать" на главной
           2) Кликаем на логотип "Самокат"
           3) Проверяем, что URL совпадает с ожидаемым и отображается заголовок "Учебный тренажер"'''
    )
    def test_scooter_logo_click(self, driver):
        header = HomePageHeader(driver)
        home_page = HomePage(driver)

        # Принимаем куки
        home_page.accept_cookie_home_page()

        # Переходим на страницу заказа, затем возвращаемся через логотип
        header.click_top_order_button()
        header.click_scooter_logo()

        # Проверяем результат
        current_url = header.get_current_url()
        title_is_visible = header.check_page_header_is_displayed()

        assert current_url == Urls.QA_SCOOTER_URL
        assert title_is_visible, "Заголовок 'Учебный тренажер' не отображается после перехода"

    @allure.title('Тест проверки перехода на Дзен по клику на логотип "Яндекс"')
    @allure.description(
        '''1) Кликаем на логотип "Яндекс"
           2) Переключаемся на новую вкладку
           3) Проверяем, что страница Дзена загрузилась и URL корректен'''
    )
    def test_yandex_logo_click(self, driver):
        header = HomePageHeader(driver)
        dzen_page = DzenPage(driver)
        home_page = HomePage(driver)

        # Принимаем куки
        home_page.accept_cookie_home_page()

        # Кликаем по логотипу Яндекса
        header.click_yandex_logo()

        # Переключаемся на новую вкладку
        header.switch_to_new_tab()

        # Ждём появления элемента на Дзене (например, кнопка "Главная")
        dzen_page.wait_for_main_button()

        # Проверяем URL
        current_url = header.get_current_url()
        assert current_url == Urls.DZEN_URL, f"Ожидался URL Дзена: {Urls.DZEN_URL}, но был: {current_url}"

    @allure.title('Тест проверки текста ответов в разделе "Вопросы о важном"')
    @allure.description(
        '''1) Скроллим к блоку вопросов
           2) Кликаем по каждому вопросу
           3) Получаем текст ответа
           4) Сравниваем с ожидаемым'''
    )
    @pytest.mark.parametrize(
        'question_locator, answer_locator, expected_text',
        zip(
            ScooterMainPageLocators.FAQ_QUESTION_BUTTONS,
            ScooterMainPageLocators.FAQ_ANSWER_PANELS,
            Questions.expected_question_text
        )
    )
    def test_accordion_questions(self, driver, question_locator, answer_locator, expected_text):
        home_page = HomePage(driver)

        # Принимаем куки
        home_page.accept_cookie_home_page()

        # Получаем текст ответа после открытия вопроса
        actual_text = home_page.get_answer_text(question_locator, answer_locator)

        # Сравниваем
        assert actual_text == expected_text, (
            f"Ожидался текст: '{expected_text}', но получен: '{actual_text}'"
        )
