import allure
import pytest

from data import Questions
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestQuestions:

    @allure.title('Проверка ответов на вопросы на главной странице Самоката')
    @pytest.mark.parametrize('question, answer, expected_answer',
                             zip(MainPageLocators.questions, MainPageLocators.answers, Questions.expected_answer))
    def test_questions_answers(self, driver, question, answer, expected_answer):
        main_page = MainPage(driver)
        main_page.click_accept_cookie_btn()
        text = main_page.get_question_text(question, answer)
        assert text == expected_answer
