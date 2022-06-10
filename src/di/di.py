from dependency_injector import containers, providers
from src.todo.todo_api_client import TodoApiClient
from src.todo.todo_service import TodoService


class DI(containers.DeclarativeContainer):
    todo_api_client = providers.Factory(TodoApiClient)
    todo_service = providers.Factory(TodoService, todo_repository=todo_api_client)
