# Web-приложение для определения заполненных форм.
### Настройка проекта:
1. Скопируйте репозиторий на вашу машину
2. Установите зависимости (_pip install -r requirements.txt_)
3. Если необходимо - внесите изменения в .env файл
### Запуск и тесты
* Для запуска тестов: _pytest_
* Для запуска проекта: _python checker.py_
### Примеры запросов
* Корректный запрос - _/get_form?email=pochta@mail.ru&date=12.12.2023&phone=+70000000000&text=helloworld_
* Еще один корректный запрос - _/get_form?email=pochta@mail.ru&phone=+70000000000_
* Некорректный запрос - _/get_form?EEEmail=pochta@mail.ru&phone=+70000000000_
* Еще один некорректный запрос - _/get_form?email=pochta@mail.ru&phone=+70000000000_
