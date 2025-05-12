import yaml
from domain.entities.task import Task

class TaskYAMLLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_tasks(self) -> list[Task]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return [Task(task["name"], task["steps"]) for task in data.get("tasks", [])]
