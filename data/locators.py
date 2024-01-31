from selenium.webdriver.common.by import By


class LocatorsMain:
    BUTTON_ORDER_MAIN = (By.XPATH, "//button[contains(text(),'Заказать')]")   #кнопка "Заказать" на главной странице. Локатор уточнен по тексту на кнопке и отвечает за кнопки вверху и внизу страницы. Они не встречаются на странице одновременно


class LocatorsOrder:
    NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="* Имя"]')                                #поле для ввода имени в окне оформления заказа
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')                       #поле для ввода фамилии в окне оформления заказа
    ADDRESS_INPUT = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')      #поле для ввода адреса, куда привезти заказ
    METRO_STATION_DROPDOWN = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')          #дропдаун станций метро
    NUMBER_PHONE = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]') #поле для ввода телефона в окне оформления заказа

    BUTTON_FUTHER = (By.XPATH, "//button[contains(text(),'Далее')]")          #промежуточная кнопка "Далее" в форме оформления заказа, переход в следующий блок

    DATA_ORDER = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")        #датапикер когда привезди самокат
    RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-control']")                         #дропдаун периода аренды
    COLOR_CHECKBOX_BLACK = (By.XPATH, ".//input[@id='black']")                             #чекбокс черного цвета самоката
    COLOR_CHECKBOX_GREY = (By.XPATH, ".//input[@id='gray']")                               #чекбокс серого цвета самоката
    COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")

    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") #кнопка "Заказать" во втором блоке формы заказа
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")                                          #кнопка с текстом "Да" для подтверждения оформления заказа

    ORDER_SUCCESS_TEXT = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")            #текст при успешном оформлении заказа

    YA_BUTTON = (By.XPATH, ".//a[@href='//yandex.ru']")  #кнопка с лого Яндекс
    SAMOKAT_IMG_BUTTON = (By.XPATH, ".//a[@href='/']")   #кнопка логотипа Самокат со ссылкой на главную страницу
