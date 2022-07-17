from flask import Blueprint, jsonify, redirect, request, render_template
from flask_login import login_required

from flask_todo.database import db_session
from flask_todo.middlewares.auth_middleware import token_required
from flask_todo.module_todo.models import Todo, todo_schema


todo_bp = Blueprint('todo', __name__)


@todo_bp.get('/todos')
@token_required
def fill_all(user):
    todos = Todo.query.filter_by(user_id=user.id).all()
    return jsonify({"code": 200, "data": [todo_schema.dump(todo) for todo in todos]})


@todo_bp.post('/todos')
@token_required
def create(user):
    data = request.json
    todo = Todo(name=data['name'], description=data['description'],
                status=data['status'], user_id=user.id)
    db_session.add(todo)
    db_session.commit()
    return jsonify({"code": 200, "message": "Create success"})
