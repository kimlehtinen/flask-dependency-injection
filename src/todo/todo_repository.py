from src.todo.todo import Todo


class TodoRepository:

    def get_todos() -> "list[Todo]":
        raise NotImplementedError
