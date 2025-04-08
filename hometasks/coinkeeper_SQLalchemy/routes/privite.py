from flask import jsonify, request, Blueprint
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from repositories.categories import create_category

# import models.db as db

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