from flask import Flask, jsonify, request, Blueprint
from http import HTTPStatus
import models.db as db

public_bp = Blueprint('public', __name__, url_prefix='/public')

@public_bp.route('/', methods=['GET'])
def ping():
    return jsonify({
        'message': 'ping was successed',
    }), HTTPStatus.OK

@public_bp.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = db.get_all_tasks()
    return jsonify({'tasks': tasks}), HTTPStatus.OK

@public_bp.route('/tasks/<int:user_id>', methods=['GET'])
def get_task_by_id(user_id):
    if user_id is None or user_id < 0:
        return jsonify({'error': 'Task id not found'}), HTTPStatus.BAD_REQUEST

    task = db.get_task_by_user_id(user_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), HTTPStatus.NOT_FOUND

    return jsonify({'task': task}), HTTPStatus.OK