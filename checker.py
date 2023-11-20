from flask import Flask, request, jsonify
from tinydb import TinyDB
from services import validator


app = Flask(__name__)
db = TinyDB('forms_db.json')


@app.route('/get_form')
def get_form():
    data = request.args.to_dict()
    validated_data = validator(data)
    form_types = ['date', 'phone', 'email', 'text']

    for template in db.all():
        template_fields = template['fields']
        template_len = len(template_fields.values())
        result = 0

        if template_fields.keys() != validated_data.keys():
            continue

        for form_type in form_types:
            if form_type in validated_data.values():
                result += 1

        if result == template_len:
            return jsonify(template["template_name"])

    return validated_data


if __name__ == '__main__':
    app.run()
