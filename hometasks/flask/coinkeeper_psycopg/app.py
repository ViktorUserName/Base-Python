from flask import Flask, jsonify, request
from http import HTTPStatus
from db import *

# from flask_jwt_extended import JWTManager


app = Flask(__name__)
# app.config["JWT_SECRET_KEY"] = "supersecretkey"
# jwt = JWTManager(app)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({
        'message': 'ping was successed',
    }), HTTPStatus.OK

@app.route('/categories', methods=['GET'])
def get_category_route():
    categories = get_all_category()
    return jsonify({'categories': categories})

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category_by_id_route(category_id):
    category = get_category_by_id(category_id)
    return jsonify({'category': category})

@app.route('/transactions/<int:category_id>', methods=['POST'])
def create_transaction_route(category_id):
    data = request.get_json()

    transaction = create_transaction(data['transaction_type'], category_id, data['user_id'], data['amount'])
    return jsonify({"transaction_id": transaction})


def main():
    try:
        # db.init_db()
        print('DB initialized successfully')
    except Exception as error:
        print(f'Error: {error}')

    try:
        app.run(port=5000, debug=True)
    except Exception as error:
        print(f'Error during server installization: {error}')

main()