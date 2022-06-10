from flask import Blueprint, jsonify
from dependency_injector.wiring import inject, Provide

from src.di.di import DI
from src.todo.todo_service import TodoService
from src.todo.todo import Todo

blueprint = Blueprint('todo_routes', __name__)

@blueprint.route("/<id>", methods=["GET"])
@inject
def get_todo(id: str, todo_service: TodoService = Provide[DI.todo_service]):
    todo: Todo = todo_service.get_todo(int(id))

    return jsonify(todo.json()), 200
