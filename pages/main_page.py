import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Скролл главной страницы до конца вниз')
    def scroll_page_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Скролл главной страницы до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
