from selenium.webdriver.common.by import By


class ConstantsData:
    METROSTATION = (By.XPATH, "//div[text()='Бульвар Рокоссовского']")
    RENT = (By.XPATH, "//div[text()='сутки']")
    COLOR_BLACK = 'чёрный жемчуг'


class ConstantsUrl:
    URL_MAIN = 'https://qa-scooter.praktikum-services.ru/'
    URL_REDIRECT = 'https://dzen.ru/'
