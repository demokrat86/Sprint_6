from selenium.webdriver.common.by import By


class MainPageLocators:
    # шапка
    logo_yandex = (By.XPATH, "//a[@class = 'Header_LogoYandex__3TSOI']")
    logo_scooter = (By.XPATH, "//a[@class = 'Header_LogoScooter__3lsAR']")
    order_btn_top = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    order_status_btn = (By.XPATH, "//button[text() = 'Статус заказа']")
    number_order_field = (By.XPATH, "//input[@class = 'Input_Input__1iN_Z Header_Input__xIoUq']")
    header_page_title = (By.XPATH, "//div[text() = 'Учебный тренажер']")

    # лендинг
    home_page_title = (By.XPATH, ".//div[@class = 'Home_Header__iJKdX']")
    order_button_low = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM')]")
    accept_cookies_btn = (By.XPATH, "//button[@id = 'rcc-confirm-button']")
    questions_title = (By.XPATH, "//div[text() = 'Вопросы о важном']")
    main_button_dzen = (By.XPATH, ".//span[text() = 'Главная']")

    # вопросы
    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    # ответы
    answers = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")]
