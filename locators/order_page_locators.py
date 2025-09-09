from selenium.webdriver.common.by import By


class ScooterOrderPageLocators:
 """
 Локаторы страницы заказа самоката.
 Включает поля формы, кнопки навигации, выбор параметров и модальные окна подтверждения.
 """

 # === Страница 1: Контактная информация ===
 NAME_INPUT = (By.XPATH, "//input@placeholder='* Имя'")
 SURNAME_INPUT = (By.XPATH, "//input@placeholder='* Фамилия'")
 ADDRESS_INPUT = (By.XPATH, "//input@placeholder='* Адрес: куда привезти заказ'")
 METRO_INPUT = (By.XPATH, "//input@placeholder='* Станция метро'")
 METRO_STATION = (By.XPATH, "//divtext()='Парк культуры'")  # Пример выбора
 PHONE_INPUT = (By.XPATH, "//input@placeholder='* Телефон: на него позвонит курьер'")
 NEXT_BUTTON = (By.XPATH, "//buttontext()='Далее'")


 # === Страница 2: Параметры заказа ===
 DELIVERY_DATE_INPUT = (By.XPATH, "//input@placeholder='* Когда привезти самокат'")
 RENT_PERIOD_DROPDOWN = (By.XPATH, "//spancontains(@class, 'Dropdown-arrow')")
 RENT_PERIOD_3_DAYS = (By.XPATH, "//divtext()='трое суток'")
 BLACK_SCOOTER_COLOR_CHECKBOX = (By.ID, "black")
 GREY_SCOOTER_COLOR_CHECKBOX = (By.ID, "grey")
 COMMENT_INPUT = (By.XPATH, "//input@placeholder='Комментарий для курьера'")
 BACK_BUTTON = (By.XPATH, "//buttontext()='Назад'")
 FINAL_ORDER_BUTTON = (By.XPATH, "(//buttontext()='Заказать')2")  # Кнопка "Заказать" на второй странице


 # === Модальное окно: Подтверждение заказа ===
 CANCEL_CONFIRMATION_BUTTON = (By.XPATH, "//buttontext()='Нет'")
 ACCEPT_CONFIRMATION_BUTTON = (By.XPATH, "//buttontext()='Да'")


 # === Модальное окно: Успешный заказ ===
 ORDER_SUCCESS_MESSAGE = (By.XPATH, "//divtext()='Заказ оформлен'")
 VIEW_STATUS_BUTTON = (By.XPATH, "//buttontext()='Посмотреть статус'")
