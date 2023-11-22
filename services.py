import re


def type_checker(value):
    phone_pattern = [r'7\d{10}$', r'\+7\d{10}$']
    value_without_spaces = value.replace(" ", "")
    if re.match(phone_pattern[0], value_without_spaces) or re.match(phone_pattern[1], value_without_spaces):
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


def template_finder(templates, data):
    form_types = ['date', 'phone', 'email', 'text']

    for template in templates:
        template_fields = template['fields']
        template_len = len(template_fields.values())
        coincidence = 0

        if template_fields.keys() != data.keys():
            continue

        for form_type in form_types:
            if form_type in data.values():
                coincidence += 1

        if coincidence == template_len:
            return template["template_name"]

    return data
