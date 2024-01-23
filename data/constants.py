from selenium.webdriver.common.by import By


class ConstantsData:
    NAME = 'Нелли'
    LASTNAME = 'См'
    ADDRESS = 'Москва'
    METROSTATION = (By.XPATH, "//div[text()='Бульвар Рокоссовского']")
    PHONE = '75555555555'
    RENT = (By.XPATH, "//div[text()='сутки']")
    COLOR = 'чёрный жемчуг'


class ConstantsUrl:
    URL_MAIN = 'https://qa-scooter.praktikum-services.ru/'
    URL_ORDER = 'https://qa-scooter.praktikum-services.ru/order'
    URL_REDIRECT = 'https://dzen.ru/'
