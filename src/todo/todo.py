class Todo:
    id: int
    title: str
    completed: bool

    def __init__(self, id: int, title: str, completed: bool) -> None:
        self.id = id
        self.title = title
        self.completed = completed

    def json(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
