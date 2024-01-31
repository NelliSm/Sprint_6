import allure
import pytest
import random
from data.constants import ConstantsUrl
from data.locators import LocatorsMain, LocatorsOrder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title('Тестирование заказа самоката')
class TestOrder:

    @allure.description('Проверка, что при нажатии первой кнопки "Заказать" вверху главной страницы, происходит '
                        'переход на страницу заказа')
    def test_check_one_button_order(self, driver):
        driver.get(ConstantsUrl.URL_MAIN)
        driver.find_element(*LocatorsMain.BUTTON_ORDER_MAIN).click()
        assert driver.current_url == f"{ConstantsUrl.URL_MAIN}order"

    @allure.description('Проверка, что при нажатии второй кнопки "Заказать" внизу главной страницы, происходит переход '
                        'на страницу заказа')
    def test_check_two_button_order(self, driver):
        order_page = MainPage(driver)
        order_page.go_to_site(ConstantsUrl.URL_MAIN)
        order_button = driver.find_element(*LocatorsMain.BUTTON_ORDER_MAIN)
        order_page.scroll_to_element(order_button)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(order_button)).click()
        assert driver.current_url == f"{ConstantsUrl.URL_MAIN}order"

    @allure.description('Создание заказа. Заполнение формы заказа с использованием в параметризации '
                        'двух наборов тестовых данных. Проверка, что появилось всплывающее окно '
                        'с сообщением об успешном создании заказа')
    @pytest.mark.parametrize("name, lastname, address, phone, comment",
                             [("Нелли", "Сметанина", f"г. Москва, ул. Мира, д.{random.randint(1, 999)}",
                               f"79000000{random.randint(100, 199)}", "Привет"),
                              ("Иван", "Крузенштерн", f"г. Москва, ул. Правды, д.{random.randint(1, 999)}",
                               f"89999999{random.randint(100, 199)}", "Пока")
                              ])
    def test_check_order_successful(self, driver, name, lastname, address, phone, comment):
        ord_page = OrderPage(driver)
        ord_page.go_to_site(f"{ConstantsUrl.URL_MAIN}order")
        ord_page.make_order(driver, name, lastname, address, phone, comment)
        completed_order = driver.find_element(*LocatorsOrder.ORDER_SUCCESS_TEXT)
        assert 'Заказ оформлен' in completed_order.text
