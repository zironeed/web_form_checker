from checker import app
from services import validator


def test_template_exists():
    """
    Тесты для существующих форм
    """
    params = {'email': 'email@mail.ru', 'date': '25.12.2023', 'phone': '+79990000000', 'text': 'textText'}
    response = app.test_client().get('/get_form', query_string=params)

    print(response.json)
    assert response.status_code == 200
    assert response.json == 'full_template'


def test_template_not_exists():
    """
    Тесты для несуществующих форм
    key_response - Проверка для данных с неверным ключом
    form_response - Проверка для набора данных, для которого нет форм
    """
    params1 = {'test_email': 'email@mail.ru', 'date': '25.12.2023', 'phone': '+79990000000', 'text': 'textText'}
    key_response = app.test_client().get('/get_form', query_string=params1)

    params2 = {'email': 'email@mail.ru'}
    form_response = app.test_client().get('/get_form', query_string=params2)

    print(key_response.json)
    assert key_response.status_code == 200
    assert key_response.json == {'date': 'date', 'phone': 'phone', 'test_email': 'email', 'text': 'text'}

    print(form_response.json)
    assert form_response.status_code == 200
    assert form_response.json == {'email': 'email'}


def test_validation():
    """
    Тесты валидации
    """
    normal_params = {'date': '25-12-2023', 'email': 'email@email.ru', 'phone': '+79990000000', 'text': 'TestText'}
    incorrect_params = {'date': '25/12/52', 'email': 'email@', 'phone': '++79990000000', 'text': 'text'}

    normal_result = validator(normal_params)
    incorrect_result = validator(incorrect_params)

    assert normal_result == {'date': 'date', 'email': 'email', 'phone': 'phone', 'text': 'text'}
    assert incorrect_result == {'date': 'text', 'email': 'text', 'phone': 'text', 'text': 'text'}
