import re


def type_checker(value):
    phone_pattern = r'7\d{10}$'
    value_without_spaces = value.replace(" ", "")
    if re.match(phone_pattern, value_without_spaces):
        return 'phone'
    elif re.match(r"[^@]+@[^@]+\.[^@]+", value_without_spaces):
        return 'email'
    else:
        return 'text'


def validator(data):
    for key, val in data.items():
        try:
            if '-' in val:
                date = val.split('-')
            else:
                date = val.split('.')

            if len(date) == 3 and int(date[1]) < 13:
                data[key] = 'date'

        finally:
            if data[key] != 'date':
                data[key] = type_checker(val)

    return data
