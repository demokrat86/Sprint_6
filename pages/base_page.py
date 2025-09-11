import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание видимости элемента')
    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Ожидание появления элемента в DOM')
    def wait_until_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    @allure.step('Ожидание, пока элемент станет кликабельным')
    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Поиск и ожидание видимости элемента')
    def find_and_wait_locator(self, locator):
        return self.wait_until_visible(locator)

    @allure.step('Клик по кнопке')
    def click_button(self, locator, timeout=10):
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

    @allure.step('Ввод текста в поле')
    def send_keys_to_field(self, locator, text):
        element = self.find_and_wait_locator(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text_locator(self, locator):
        return self.find_and_wait_locator(locator).text

    @allure.step('Прокрутка к элементу')
    def scroll_to_element(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Переключение на новую вкладку')
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
