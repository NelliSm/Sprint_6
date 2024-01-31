import pytest
import allure
import keyboard
from data.locators import LocatorsOrder
from pages.base_page import BasePage
from data.constants import ConstantsData


class OrderPage(BasePage):

    @allure.step('Метод заполнения формы заказа. '
                 'Клик на промежуточную кнопку "Далее" и "Сделать заказ"')
    def make_order(self, driver, name, lastname, address, phone, comment):
        driver.find_element(*LocatorsOrder.NAME_INPUT).send_keys(name)
        driver.find_element(*LocatorsOrder.LAST_NAME_INPUT).send_keys(lastname)
        driver.find_element(*LocatorsOrder.ADDRESS_INPUT).send_keys(address)
        driver.find_element(*LocatorsOrder.METRO_STATION_DROPDOWN).click()
        driver.find_element(*ConstantsData.METROSTATION).click()
        driver.find_element(*LocatorsOrder.NUMBER_PHONE).send_keys(phone)
        driver.find_element(*LocatorsOrder.BUTTON_FUTHER).click()
        driver.find_element(*LocatorsOrder.DATA_ORDER).click()
        keyboard.press('enter')
        driver.find_element(*LocatorsOrder.RENTAL_PERIOD).click()
        driver.find_element(*ConstantsData.RENT).click()
        driver.find_element(*LocatorsOrder.COLOR_CHECKBOX_BLACK).click()
        driver.find_element(*LocatorsOrder.COMMENT).click()
        driver.find_element(*LocatorsOrder.COMMENT).send_keys(comment)
        driver.find_element(*LocatorsOrder.BUTTON_ORDER).click()
        driver.find_element(*LocatorsOrder.BUTTON_YES).click()
