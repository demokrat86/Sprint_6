import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнить поле Имя')
    def filling_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.name_field, text)

    @allure.step('Заполнить поле Фамилия')
    def filling_last_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.last_name_field, text)

    @allure.step('Заполнить поле Адрес')
    def filling_address_field(self, text):
        self.send_keys_to_field(OrderPageLocators.address_field, text)

    @allure.step('Заполнить поле Станция метро')
    def pick_up_metro_station(self, text):
        self.click_button(OrderPageLocators.metro_station_field)
        self.send_keys_to_field(OrderPageLocators.metro_station_field, text)
        self.click_button(OrderPageLocators.station_metro)

    @allure.step('Заполнить поле Номер телефона')
    def filling_telephone_number_field(self, text):
        self.send_keys_to_field(OrderPageLocators.telephone_field, text)

    @allure.step('Клик по кнопке Далее')
    def click_next_button(self):
        self.click_button(OrderPageLocators.next_button)

    @allure.step('Заполнение формы Для кого самокат')
    def filling_first_order_form(self, user):
        self.filling_name_field(user[0])
        self.filling_last_name_field(user[1])
        self.filling_address_field(user[2])
        self.pick_up_metro_station(user[3])
        self.filling_telephone_number_field(user[4])
        self.click_next_button()

    @allure.step('Выбор даты Когда привезти заказ')
    def pick_up_deliver_date(self, text):
        self.click_button(OrderPageLocators.deliver_order_field)
        self.send_keys_to_field(OrderPageLocators.deliver_order_field, text)

    @allure.step('Выбор срока аренды')
    def select_rent_time(self):
        self.click_button(OrderPageLocators.rent_period_field)
        self.click_button(OrderPageLocators.rent_period_three_days)

    @allure.step('Выбор цвета самоката')
    def select_color_scooter(self):
        self.click_button(OrderPageLocators.black_color_scooter_check)

    @allure.step('Заполнение поля Комментарии для курьера')
    def send_comment_to_comment_field(self, text):
        self.send_keys_to_field(OrderPageLocators.comment_field, text)

    @allure.step('Клик по кнопке Заказать')
    def click_order_button(self):
        self.click_button(OrderPageLocators.order_button)

    @allure.step('Заполнение формы Про аренду')
    def filling_second_order_form(self, text):
        self.pick_up_deliver_date(text[5])
        self.select_rent_time()
        self.select_color_scooter()
        self.send_comment_to_comment_field(text[6])
        self.click_order_button()

    @allure.step('Клик на кнопку Да')
    def click_yes_order_scooter(self):
        self.click_button(OrderPageLocators.yes_button)

    @allure.step('Проверка успешного бронирования заказа')
    def check_order_title(self):
        return self.find_and_wait_locator(OrderPageLocators.order_placed_text).is_displayed()
