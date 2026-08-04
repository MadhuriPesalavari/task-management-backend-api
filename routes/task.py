from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from extensions import db
from models.task import Task

# Validator import
from utils.validators import validate_task_status

task_bp = Blueprint(
    'task',
    __name__,
    url_prefix='/tasks'
)


# Create Task
@task_bp.route('', methods=['POST'])
@jwt_required()
def create_task():

    current_user = get_jwt_identity()

    data = request.get_json()

    task = Task(
        title=data['title'],
        description=data['description'],
        user_id=current_user
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({
        "message": "Task Created"
    }), 201


# Get All Tasks
@task_bp.route('', methods=['GET'])
@jwt_required()
def get_tasks():

    current_user = get_jwt_identity()

    tasks = Task.query.filter_by(
        user_id=current_user
    ).all()

    output = []

    for task in tasks:
        output.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        })

    return jsonify(output)


# Get Single Task
@task_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_task(id):

    current_user = get_jwt_identity()

    task = Task.query.filter_by(
        id=id,
        user_id=current_user
    ).first()

    if not task:
        return jsonify({
            "message": "Task not found"
        }), 404

    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    })


# Update Task
@task_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):

    current_user = get_jwt_identity()

    task = Task.query.filter_by(
        id=id,
        user_id=current_user
    ).first()

    if not task:
        return jsonify({
            "message": "Task not found"
        }), 404

    data = request.get_json()

    if "title" in data:
        task.title = data["title"]

    if "description" in data:
        task.description = data["description"]

    if "status" in data:

        if not validate_task_status(data["status"]):
            return jsonify({
                "message": "Status must be Pending, In Progress or Completed"
            }), 400

        task.status = data["status"]

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully"
    })


# Delete Task
@task_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):

    current_user = get_jwt_identity()

    task = Task.query.filter_by(
        id=id,
        user_id=current_user
    ).first()

    if not task:
        return jsonify({
            "message": "Task not found"
        }), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    })