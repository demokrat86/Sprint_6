import allure

from locators.order_page_locators import ScooterOrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    """
    Страница: Форма заказа самоката
    Методы для заполнения обеих страниц формы, подтверждения заказа и проверки результата.
    """

    @allure.step('Заполнение поля "Имя"')
    def fill_name_field(self, name: str):
        self.send_keys_to_field(ScooterOrderPageLocators.NAME_INPUT, name)

    @allure.step('Заполнение поля "Фамилия"')
    def fill_surname_field(self, surname: str):
        self.send_keys_to_field(ScooterOrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Заполнение поля "Адрес"')
    def fill_address_field(self, address: str):
        self.send_keys_to_field(ScooterOrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбор станции метро')
    def select_metro_station(self, station: str = 'Парк культуры'):
        self.click_element(ScooterOrderPageLocators.METRO_INPUT)
        self.send_keys_to_field(ScooterOrderPageLocators.METRO_INPUT, station)
        self.click_element(ScooterOrderPageLocators.METRO_STATION)

    @allure.step('Заполнение поля "Телефон"')
    def fill_phone_field(self, phone: str):
        self.send_keys_to_field(ScooterOrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Клик на кнопку "Далее"')
    def click_next_button(self):
        self.click_element(ScooterOrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение первой страницы формы: "Для кого самокат"')
    def fill_first_page(self, user):
        """
        user: список или кортеж вида
        [name, surname, address, metro, phone, ...]
        """
        self.fill_name_field(user[0])
        self.fill_surname_field(user[1])
        self.fill_address_field(user[2])
        self.select_metro_station(user[3])
        self.fill_phone_field(user[4])
        self.click_next_button()

    @allure.step('Указание даты доставки')
    def fill_delivery_date(self, date: str):
        self.click_element(ScooterOrderPageLocators.DELIVERY_DATE_INPUT)
        self.send_keys_to_field(ScooterOrderPageLocators.DELIVERY_DATE_INPUT, date)

    @allure.step('Выбор срока аренды — трое суток')
    def select_rent_period(self):
        self.click_element(ScooterOrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_element(ScooterOrderPageLocators.RENT_PERIOD_3_DAYS)

    @allure.step('Выбор цвета самоката — чёрный')
    def select_black_color(self):
        self.click_element(ScooterOrderPageLocators.BLACK_SCOOTER_COLOR_CHECKBOX)

    @allure.step('Выбор цвета самоката — серый')
    def select_grey_color(self):
        self.click_element(ScooterOrderPageLocators.GREY_SCOOTER_COLOR_CHECKBOX)

    @allure.step('Указание комментария для курьера')
    def fill_comment_field(self, comment: str):
        self.send_keys_to_field(ScooterOrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Клик на кнопку "Заказать" (на второй странице)')
    def click_final_order_button(self):
        self.click_element(ScooterOrderPageLocators.FINAL_ORDER_BUTTON)

    @allure.step('Заполнение второй страницы формы: "Про аренду"')
    def fill_second_page(self, user):
        self.fill_delivery_date(user[5])
        self.select_rent_period()
        self.select_black_color()  # можно добавить выбор цвета как параметр
        self.fill_comment_field(user[6])
        self.click_final_order_button()

    @allure.step('Отмена подтверждения заказа')
    def cancel_order(self):
        self.click_element(ScooterOrderPageLocators.CANCEL_CONFIRMATION_BUTTON)

    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.click_element(ScooterOrderPageLocators.ACCEPT_CONFIRMATION_BUTTON)

    @allure.step('Полный путь заказа: от первой до последней страницы')
    def order_scooter_full_path(self, user):
        """
        Полный сценарий заказа:
        1) Заполнение данных клиента
        2) Заполнение параметров аренды
        3) Подтверждение заказа
        """
        self.fill_first_page(user)
        self.fill_second_page(user)
        self.confirm_order()

    @allure.step('Проверка: появилось ли окно "Заказ оформлен"')
    def check_order_confirmation_title(self) -> bool:
        element = self.find_and_wait_locator(ScooterOrderPageLocators.ORDER_SUCCESS_MESSAGE)
        return element.is_displayed() if element else False
