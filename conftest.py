import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service  # ← Добавлено!
from webdriver_manager.firefox import GeckoDriverManager  # ← Добавлено!
from helps.data import Urls

# Отключаем проверку SSL (для Windows 7)
import os
os.environ['WDM_SSL_VERIFY'] = '0'

@pytest.fixture
def driver():
    # Путь к вашему geckodriver
    driver_path = r"C:\projects\Sprint_6\geckodriver.exe"
    service = Service(driver_path)
    driver = webdriver.Firefox(service=service)
    driver.get(Urls.QA_SCOOTER_URL)
    yield driver
    driver.quit()