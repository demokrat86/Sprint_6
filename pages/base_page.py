from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_visible(self, locator, timeout=10):
        """Ожидание видимости элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_present(self, locator, timeout=10):
        """Ожидание появления элемента в DOM"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_until_clickable(self, locator, timeout=10):
        """Ожидание, пока элемент станет кликабельным"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    def find_and_wait_locator(self, locator):
        """Поиск и ожидание видимости элемента (для чтения текста и т.п.)"""
        return self.wait_until_visible(locator)

    def click_button(self, locator, timeout=10):
        """
        Универсальный метод для клика по кнопке.
        1. Прокручивает к элементу.
        2. Ждёт, пока станет кликабельным.
        3. Пытается обычный клик.
        4. Если не получается — использует JavaScript.
        """
        # Прокручиваем к элементу
        element = self.find_and_wait_locator(locator)
        ActionChains(self.driver).move_to_element(element).perform()

        # Ждём, пока элемент станет кликабельным
        try:
            element = self.wait_until_clickable(locator, timeout)
            element.click()
        except ElementClickInterceptedException:
            # Если клик перехвачен — используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            raise TimeoutException(f"Элемент {locator} не стал кликабельным за {timeout} секунд")

    def send_keys_to_field(self, locator, text):
        """Ввод текста в поле"""
        element = self.find_and_wait_locator(locator)
        element.clear()  # Очистка поля перед вводом (рекомендуется)
        element.send_keys(text)

    def get_text_locator(self, locator):
        """Получение текста элемента"""
        return self.find_and_wait_locator(locator).text

    def scroll_to_locator(self, locator):
        """Прокрутка к элементу"""
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def go_to_new_tab(self):
        """Переключение на новую вкладку"""
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_element(self, locator):
        """Проверка, что элемент отображается"""
        return self.find_and_wait_locator(locator).is_displayed()
