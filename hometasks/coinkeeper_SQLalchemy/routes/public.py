from flask import jsonify, request, Blueprint
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity

from repositories.categories import get_all_categories

public_bp = Blueprint('public', __name__, url_prefix='/public')

@public_bp.route('/categories', methods=['GET'])
def get_all_categories_route():
    data = get_all_categories()
    return jsonify(data)
