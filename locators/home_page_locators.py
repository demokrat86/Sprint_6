from selenium.webdriver.common.by import By


class ScooterHomePageLocators:
    """
    Локаторы для хедера и основной страницы сервиса «Самокат за 1 клик».
    Используются в UI-тестах для взаимодействия с элементами главной страницы.
    """

    # === Хедер ===
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    TOP_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[text()='Статус заказа']")
    ORDER_NUMBER_INPUT = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    GO_BUTTON = (By.XPATH, "//button[text()='Go']")
    VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть']")
    PAGE_HEADER = (By.XPATH, "//div[text()='Учебный тренажер']")


class ScooterMainPageLocators:
    """
    Локаторы для контентной части главной страницы.
    Включает заголовок, кнопки, вопросы и ответы из раздела «Вопросы о важном».
    """

    # === Основные элементы ===
    MAIN_TITLE = (By.XPATH, "//div[contains(@class, 'Home_Header')]")
    QUESTIONS_TITLE = (By.XPATH, "//div[text()='Вопросы о важном']")
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # === Вопросы и ответы (FAQ) ===
    # Заголовки вопросов
    FAQ_QUESTION_BUTTONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    # Тексты ответов (появляются после клика по вопросу)
    FAQ_ANSWER_PANELS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]
