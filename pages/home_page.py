from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import ScooterHomePageLocators, ScooterMainPageLocators
from pages.base_page import BasePage


class HomePageHeader(BasePage):
    """
    Page Object: Хедер главной страницы.
    Содержит методы для взаимодействия с логотипами и кнопками в шапке.
    """

    def click_yandex_logo(self):
        """Кликаем по логотипу Яндекса"""
        self.click_element(ScooterHomePageLocators.YANDEX_LOGO)

    def click_scooter_logo(self):
        """Кликаем по логотипу Самоката"""
        self.click_element(ScooterHomePageLocators.SCOOTER_LOGO)

    def click_top_order_button(self):
        """Кликаем по верхней кнопке 'Заказать'"""
        self.click_element(ScooterHomePageLocators.TOP_ORDER_BUTTON)

    def click_order_status_button(self):
        """Кликаем по кнопке 'Статус заказа'"""
        self.click_element(ScooterHomePageLocators.ORDER_STATUS_BUTTON)

    def switch_to_new_tab(self):
        """Переключаемся на новую вкладку"""
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        """Получаем текущий URL"""
        return self.driver.current_url

    def check_page_header_is_displayed(self):
        """Проверяем, что заголовок 'Учебный тренажёр' отображается"""
        header_locator = (By.XPATH, "//div[contains(@class, 'Home_Header')]//h1[text()='Учебный тренажёр']")
        return self.is_element_visible(header_locator)


class HomePage(BasePage):
    """
    Page Object: Главная страница.
    Содержит методы для работы с куками, скроллом и FAQ.
    """

    def accept_cookie_home_page(self):
        """Принимаем куки"""
        self.click_element(ScooterMainPageLocators.COOKIE_ACCEPT_BUTTON)

    def scroll_and_click_bottom_order_button(self):
        """Скроллим к нижней кнопке 'Заказать' и кликаем"""
        self.scroll_to_locator(ScooterHomePageLocators.BOTTOM_ORDER_BUTTON)
        self.click_element(ScooterHomePageLocators.BOTTOM_ORDER_BUTTON)

    def scroll_to_faq_block(self):
        """Скроллим к блоку 'Вопросы о важном'"""
        self.scroll_to_locator(ScooterMainPageLocators.FAQ_SECTION)

    def get_answer_text(self, question_locator, answer_locator):
        """
        Кликаем по вопросу и получаем текст ответа
        :param question_locator: локатор вопроса
        :param answer_locator: локатор панели ответа
        :return: текст ответа
        """
        self.click_element(question_locator)
        return self.get_text_from_element(answer_locator)
