from selenium.webdriver.common.by import By


class DzenPageLocators:
    """
    Локаторы для страницы Дзена.
    Используются в DzenPage (Page Object).
    """
    NAV_HOME_BUTTON = (By.XPATH, "//span[normalize-space(text())='Главная']")
    LOGO = (By.XPATH, "//a[@aria-label='Дзен']")
    TOPICS_FEED = (By.XPATH, "//div[contains(@class, 'topics-feed')]")
