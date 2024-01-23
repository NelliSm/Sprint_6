# Sprint_6

- Установить зависимости для запуска тестов:

pip3 install -r requirements.txt 



- Для запуска тестов:
pytest -v tests.py 


Tests:

1. Тест проверяет если нажать на логотип «Самоката», происходит переход на главную страницу «Самоката». Если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена:
test_click_on_logo


2. Тест проверяет если нажать на стрелочку, открывается соответствующий текст. Происходит тест на каждый вопрос с помощью параметризации:
test_list_FAQ_section


3. Заказ самоката. Тест проверяет заказ самоката с разными данными. Отдельными методами проверяются точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу:
test_order_successful
