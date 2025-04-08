from flask import jsonify, request, Blueprint
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from repositories.categories import create_category
from repositories.users import update_balance
from repositories.transactions import create_transaction


private_bp = Blueprint('privite', __name__, url_prefix='/privite')

@private_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    try:
        return jsonify({"message": f"Hello, user {user_id}!"}), HTTPStatus.OK
    except Exception as e:
        print(e)

@private_bp.route('/categories', methods=['POST'])
@jwt_required()
def create_category_route():
    user_id = get_jwt_identity()
    try:
        data = request.get_json()
        title = data.get('title')

        if not title:
            return jsonify({"message": "title is required"}), HTTPStatus.BAD_REQUEST

        result = create_category(title, user_id)
        if 'error' in result:
            return jsonify(result), HTTPStatus.BAD_REQUEST
        else:
            return jsonify(result), HTTPStatus.OK

    except Exception as e:
        return jsonify({"message": str(e)}), HTTPStatus.BAD_REQUEST


@private_bp.route('/users', methods=['PATCH'])
@jwt_required()
def update_balance_route():
    user_id = get_jwt_identity()
    try:
        data = request.get_json()
        balance = data.get('balance')

        if balance is None:
            return jsonify({'message': 'balance is required'}), HTTPStatus.BAD_REQUEST

        result = update_balance(user_id, balance)

        if not result:
            return jsonify({'message': 'User not found'}), HTTPStatus.NOT_FOUND

        return jsonify({'new_balance': result}), HTTPStatus.OK

    except Exception as e:
        return jsonify({'message': str(e)}), HTTPStatus.BAD_REQUEST

@private_bp.route('/transactions/<int:category_id>', methods=['POST'])
@jwt_required()
def create_transaction_route(category_id):
    user_id = get_jwt_identity()
    try:
        data = request.get_json()
        transaction = create_transaction(user_id,category_id,data['transaction_type'], data['amount'])
        if 'error' in transaction:
            return jsonify(transaction), HTTPStatus.BAD_REQUEST
        else:
            return jsonify(transaction), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({'message': str(e)}), HTTPStatus.BAD_REQUEST
