import allure
from data.constants import ConstantsUrl
from data.locators import LocatorsMain, LocatorsOrder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.title('Тестирование заказа самоката')
class TestOrder:

    @allure.description('Проверка, что при нажатии первой кнопки "Заказать" вверху главной страницы происходит '
                        'переход на страницу заказа')
    def test_check_one_button_order(self, driver):
        driver.get(ConstantsUrl.URL_MAIN)
        driver.find_element(*LocatorsMain.BUTTON_ORDER_TOP).click()
        assert driver.current_url == ConstantsUrl.URL_ORDER

    @allure.description('Проверка, что при нажатии второй кнопки "Заказать" внизу главной страницы происходит переход '
                        'на страницу заказа')
    def test_check_two_button_order(self, driver):
        order_page = MainPage(driver)
        order_page.go_to_site(ConstantsUrl.URL_MAIN)
        order_button = driver.find_element(*LocatorsMain.BUTTON_ORDER_BOTTOM)
        order_page.scroll_to_element(order_button)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(order_button)).click()
        assert driver.current_url == ConstantsUrl.URL_ORDER

    @allure.description('Создание заказа. Заполнение формы заказа. Проверка, что появилось всплывающее окно с '
                        'сообщением об успешном создании заказа')
    def test_order_scooter(self, driver):
        ord_page = OrderPage(driver)
        ord_page.go_to_site(ConstantsUrl.URL_ORDER)
        ord_page.make_order(driver)
        completed_order = driver.find_element(*LocatorsOrder.ORDER_SUCCESS_TEXT)
        assert 'Заказ оформлен' in completed_order.text
