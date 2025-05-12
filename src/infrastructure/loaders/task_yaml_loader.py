import yaml
from domain.entities.task import Task

class TaskYAMLLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_tasks(self) -> list[Task]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return [
            Task(
                name=task_name,
                description=task_data["description"],
                expected_output=task_data["expected_output"],
                output_example=task_data.get("output_example")
            )
            for task_name, task_data in data.items()
        ]
