import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик по лого Яндекса')
    def click_yandex_logo(self):
        self.click_button(MainPageLocators.logo_yandex)

    @allure.step('Клик по лого Самоката')
    def click_scooter_logo(self):
        self.click_button(MainPageLocators.logo_scooter)

    @allure.step('Клик по кнопке Заказать')
    def click_order_button(self):
        self.click_button(MainPageLocators.order_btn_top)

    @allure.step('Проверка надпись "Учебный проект" отображается')
    def check_order_title_displaying(self):
        return self.find_and_wait_locator(MainPageLocators.header_page_title).is_displayed()

    @allure.step('Клик на кнопку Принять куки')
    def click_accept_cookie_btn(self):
        self.click_button(MainPageLocators.accept_cookies_btn)

    @allure.step('Переход к разделу с вопросами')
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.questions_title)

    @allure.step('Клик по вопросу')
    def click_question_button(self, question_button_locator):
        self.scroll_to_questions()
        self.click_button(question_button_locator)

    @allure.step('Получение текста вопроса')
    def get_question_text(self, question_locator, answer_locator):
        self.click_question_button(question_locator)
        text_question = self.get_text_locator(answer_locator)
        return text_question

    @allure.step('Проверка отображения кнопки "Главная" на странице DZEN')
    def check_element_main_button(self):
        return self.wait_until_present(MainPageLocators.main_button_dzen, timeout=5)
