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
        scooter.go_to_site(ConstantsUrl.URL_ORDER)
        scooter.click(LocatorsOrder.SAMOKAT_IMG_BUTTON)
        assert driver.current_url == ConstantsUrl.URL_MAIN

    @allure.description('Проверка перехода на сайт /dzen.ru при клике на лого Яндекс. Ожидание загрузки новой '
                        'страницы. Проверка, что после закрытия нового окна, оказываемся на странице заказа Самоката')
    def test_click_on_yandex_logo_check_redirect(self, driver):
        ya_logo = OrderPage(driver)
        ya_logo.go_to_site(ConstantsUrl.URL_ORDER)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles
        ya_logo.click(LocatorsOrder.YA_BUTTON)
        WebDriverWait(driver, 5).until(expected_conditions.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        WebDriverWait(driver, 10).until(
            expected_conditions.url_contains(ConstantsUrl.URL_REDIRECT))
        driver.close()
        driver.switch_to.window(current_window)
        assert driver.current_url == ConstantsUrl.URL_ORDER
