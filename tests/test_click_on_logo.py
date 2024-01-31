import allure
from data.constants import ConstantsUrl
from data.locators import LocatorsOrder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.order_page import OrderPage


@allure.title('Проверка перехода по логотипам на странице заказа')
class TestLogoClick:

    @allure.description('Проверка перехода на гланую страницу Самоката при клике на лого Самокат')
    def test_click_on_scooter_logo(self, driver):
        scooter = OrderPage(driver)
        scooter.go_to_site(f"{ConstantsUrl.URL_MAIN}order")
        driver.find_element(*LocatorsOrder.SAMOKAT_IMG_BUTTON).click()
        assert driver.current_url == ConstantsUrl.URL_MAIN

#Тест клика на Яндекс разделила на два метода проверки
    @allure.description('Проверка, что при клике на лого Яндекс открывается новое окно')
    def test_click_on_yandex_logo_check_open_new_window(self, driver):
        ya_logo = OrderPage(driver)
        ya_logo.go_to_site(f"{ConstantsUrl.URL_MAIN}order")
        old_windows = driver.window_handles
        driver.find_element(*LocatorsOrder.YA_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.new_window_is_opened(old_windows))
        assert len(driver.window_handles) == len(old_windows) + 1

    @allure.description('Проверка, по клику на Яндекс при переходе в новое окно, текущий url содержит /dzen.ru')
    def test_click_on_yandex_logo_check_redirected_to_new_window(self, driver):
        ya_logo = OrderPage(driver)
        ya_logo.go_to_site(f"{ConstantsUrl.URL_MAIN}order")
        driver.find_element(*LocatorsOrder.YA_BUTTON).click()
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)
        WebDriverWait(driver, 3).until(expected_conditions.url_contains(ConstantsUrl.URL_REDIRECT))
        assert 'https://dzen.ru/' in driver.current_url
