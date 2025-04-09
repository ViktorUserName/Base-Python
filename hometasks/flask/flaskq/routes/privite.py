from flask import jsonify, request, Blueprint
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
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

@private_bp.route('/tasks', methods=['POST'])
@jwt_required()
def add_task():
    user_id = get_jwt_identity()
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(f'error reading json: {e}'),HTTPStatus.BAD_REQUEST

    if data is None:
        return jsonify({"message": "No data"}), HTTPStatus.BAD_REQUEST
    elif 'title' not in data or 'description' not in data or data['title'] == '' or data['description'] == '':
        return jsonify({"message": "data is '' or None"}), HTTPStatus.BAD_REQUEST

    task_id = db.create_new_task(user_id, data['title'], data['description'])
    if not task_id:
        return jsonify({"message": "Task creation failed"}), HTTPStatus.BAD_REQUEST

    return jsonify({'message': 'task created', "task_id": task_id}), HTTPStatus.CREATED

@private_bp.route('/tasks/<task_id>', methods=['POST'])
@jwt_required()
def add_subtask(task_id):
    user_id = get_jwt_identity()
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(f'error reading json: {e}'), HTTPStatus.BAD_REQUEST

    if data is None:
        return jsonify({"message": "No data"}), HTTPStatus.BAD_REQUEST
    elif 'title' not in data or data['title'] == '':
        return jsonify({"message": "data is '' or None"}), HTTPStatus.BAD_REQUEST

    if not db.is_task_belongs_to_user(user_id, task_id):
        return jsonify({"message": "Task dont belong to user"}), HTTPStatus.FORBIDDEN

    subtask_id = db.create_subtask_by_task_id(task_id, data['title'])
    if not subtask_id:
        return jsonify({"message": "Subtask creation failed"}), HTTPStatus.BAD_REQUEST

    return jsonify({'message': 'subtask created', "subtask": subtask_id}), HTTPStatus.CREATED

@private_bp.route('/tasks/<task_id>', methods=['PUT'])
@jwt_required()
def update_task_route(task_id):
    user_id = get_jwt_identity()

    try:
        data = request.get_json()
    except Exception as e:
        return jsonify(f'Error reading JSON: {e}'), HTTPStatus.BAD_REQUEST

    if not data:
        return jsonify({"message": "No data"}), HTTPStatus.BAD_REQUEST

    if not db.is_task_belongs_to_user(user_id, task_id):
        return jsonify({"message": "Task doesn't belong to the user"}), HTTPStatus.FORBIDDEN

    updated_task_id = db.update_task(data['title'], data['description'], task_id, user_id)

    if not updated_task_id:
        return jsonify({"message": "Task update failed"}), HTTPStatus.BAD_REQUEST

    return jsonify({'message': 'Task updated', "task_id": updated_task_id}), HTTPStatus.OK

@private_bp.route('/tasks/<task_id>', methods=['DELETE'])
@jwt_required()
def delete_task_route(task_id):
    user_id = get_jwt_identity()

    if task_id is None or int(task_id) <= 0:
        return jsonify({'error': 'Invalid post id'}), HTTPStatus.BAD_REQUEST
    if not db.is_task_belongs_to_user(user_id, task_id):
        return jsonify({"message": "Task doesn't belong to the user"}), HTTPStatus.FORBIDDEN

    deleted_task_id = db.delete_task(task_id, user_id)

    if deleted_task_id is None:
        return jsonify({"message": "Task not found or already deleted"}), HTTPStatus.NOT_FOUND

    return jsonify({'message': 'Task deleted'}), HTTPStatus.OK