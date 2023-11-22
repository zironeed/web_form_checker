from flask import Flask, request, jsonify
from tinydb import TinyDB
from dotenv import load_dotenv
import os

from services import validator, template_finder

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


app = Flask(__name__)
db = TinyDB(os.getenv('DB_NAME'))


@app.route('/get_form')
def get_form():
    data = request.args.to_dict()
    validated_data = validator(data)
    result = template_finder(db.all(), validated_data)

    return jsonify(result)


if __name__ == '__main__':
    app.run()
