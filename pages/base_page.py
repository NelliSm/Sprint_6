import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на сайт')
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step('Кликнуть на элемент')
    def click(self, locator):
        self.driver.find_element(*locator).click()
