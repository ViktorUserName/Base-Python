from flask import Flask, jsonify, request, Blueprint
from http import HTTPStatus
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import models.db as db

private_bp = Blueprint('privite', __name__, url_prefix='/privite')

@private_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    try:
        return jsonify({"message": f"Hello, user {user_id}!"}), HTTPStatus.OK
    except Exception as e:
        print(e)

