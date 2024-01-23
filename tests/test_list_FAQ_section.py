import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.constants import ConstantsUrl
from pages.main_page import MainPage


@allure.title('Проверка соответствия ответов в разделе «Вопросы о важном».')
class TestFAQ:

    @pytest.mark.parametrize('question, expected_answer', [
        ("Сколько это стоит? И как оплатить?", "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        ("Хочу сразу несколько самокатов! Так можно?",
         "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать "
         "несколько заказов — один за другим."),
        ("Как рассчитывается время аренды?",
         "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды "
         "начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, "
         "суточная аренда закончится 9 мая в 20:30."),
        ("Можно ли заказать самокат прямо на сегодня?",
         "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        ("Можно ли продлить заказ или вернуть самокат раньше?",
         "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        ("Вы привозите зарядку вместе с самокатом?",
         "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без "
         "передышек и во сне. Зарядка не понадобится."),
        ("Можно ли отменить заказ?",
         "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        ("Я жизу за МКАДом, привезёте?", "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    @allure.description(
        'тест соответствия текста ожидаемого ответа на вопрос. Для проверки всех значений используется параметризация')
    def test_questions_important_things_and_answer_correct(self, driver, question, expected_answer):
        main_page = MainPage(driver)
        main_page.go_to_site(ConstantsUrl.URL_MAIN)
        main_page.scroll_page_end()
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(
            (By.XPATH, f"//div[contains(text(),'{question}')]"))).click()
        answer_element = WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(
            (By.XPATH, f"//p[contains(text(), '{expected_answer}')]")))
        assert expected_answer == answer_element.text, (f'Ожидался ответ: "{expected_answer}", '
                                                        f'получено: "{answer_element}"')
