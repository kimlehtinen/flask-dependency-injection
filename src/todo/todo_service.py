from src.todo.todo_repository import TodoRepository
from src.todo.todo import Todo


class TodoService:
    _todo_repository: TodoRepository

    def __init__(self, todo_repository: TodoRepository) -> None:
        self._todo_repository = todo_repository

    def get_todo(self, id: int) -> Todo:
        todos: "list[Todo]" = self._todo_repository.get_todos()
    
        todo: Todo = next((x for x in todos if x.id == id), None)

        return todo
