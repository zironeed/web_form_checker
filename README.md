# Web-приложение для определения заполненных форм.
### Настройка проекта:
1. Скопируйте репозиторий на вашу машину
2. Установите зависимости (_pip install -r requirements.txt_)
### Запуск и тесты
* Для запуска тестов: _pytest .\tests.py_
* Для запуска проекта: _python checker.py_
### Примеры запросов
* Корректный запрос - _/get_form?email=pochta@mail.ru&date=25.12.2002&phone=+79874874655&text=helloworld_
* Еще один корректный запрос - _/get_form?email=pochta@mail.ru&phone=+79874874655_
* Некорректный запрос - _/get_form?EEEmail=pochta@mail.ru&phone=+79874874655_
* Еще один некорректный запрос - _/get_form?mail=pochta@mail.ru&phone=+779874874655_
