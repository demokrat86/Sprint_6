from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators
import allure

class DzenPage(BasePage):

    @allure.step('Проверка отображения кнопки "Главная" на странице DZEN')
    def check_element_main_button(self):
        return self.wait_until_present(DzenPageLocators.main_button_dzen, timeout=5)