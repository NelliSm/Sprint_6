import allure
import keyboard
from data.constants import ConstantsData
from data.data_random import DataRandom
from data.locators import LocatorsOrder
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение формы заказа константами и рандомными значениями. Клик на промежуточную кнопку "Далее" и '
                 '"Сделать заказ"')
    def make_order(self, driver):
        driver.find_element(*LocatorsOrder.NAME_INPUT).send_keys(*ConstantsData.NAME)
        driver.find_element(*LocatorsOrder.LAST_NAME_INPUT).send_keys(*ConstantsData.LASTNAME)
        driver.find_element(*LocatorsOrder.ADDRESS_INPUT).send_keys(*DataRandom.address)
        driver.find_element(*LocatorsOrder.METRO_STATION_DROPDOWN).click()
        driver.find_element(*ConstantsData.METROSTATION).click()
        driver.find_element(*LocatorsOrder.NUMBER_PHONE).send_keys(*DataRandom.phone)
        driver.find_element(*LocatorsOrder.BUTTON_FURTHER).click()
        driver.find_element(*LocatorsOrder.DATA_ORDER).click()
        keyboard.press('enter')
        driver.find_element(*LocatorsOrder.RENTAL_PERIOD).click()
        driver.find_element(*ConstantsData.RENT).click()
        driver.find_element(*LocatorsOrder.COLOR_CHECKBOX_BLACK).click()
        driver.find_element(*LocatorsOrder.BUTTON_ORDER).click()
        driver.find_element(*LocatorsOrder.BUTTON_YES).click()
