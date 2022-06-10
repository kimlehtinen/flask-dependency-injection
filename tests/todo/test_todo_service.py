from src.todo.todo_repository import TodoRepository
from src.todo.todo import Todo
from src.todo.todo_service import TodoService


class MockTodoRepistory(TodoRepository):
    _todos: "list[Todo]"
    
    def __init__(self, todos: "list[Todo]") -> None:
        self._todos = todos

    def get_todos(self) -> "list[Todo]":
        return self._todos



def test_get_todo__finds_todo():
    todos: "list[Todo]" = [
        Todo(id=1, title="todo1", completed=False),
        Todo(id=2, title="todo2", completed=False)
    ]

    mock_todo_repository = MockTodoRepistory(todos=todos)
    todo_service = TodoService(todo_repository=mock_todo_repository)
    
    todo = todo_service.get_todo(id=1)

    assert todo.title == "todo1"
