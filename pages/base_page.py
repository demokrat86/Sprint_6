from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_present(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def get_current_url(self):
        return self.driver.current_url

    def find_and_wait_locator(self, locator):
        return self.wait_until_visible(locator, timeout=10)

    def click_button(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)

    def get_text_locator(self, locator):
        return self.find_and_wait_locator(locator).text

    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_element(self, locator):
        return self.find_and_wait_locator(locator).is_displayed()
