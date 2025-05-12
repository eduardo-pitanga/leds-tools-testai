from src.domain.entities.task import Task

class TaskLoader:
    def __init__(self):
        pass

    def load_tasks(self, tasks_dict: dict) -> list[Task]:
        """
        Carrega as tarefas a partir de um dicionário fornecido.

        :param tasks_dict: Dicionário contendo as configurações das tarefas.
        :return: Lista de objetos Task.
        """
        return [
            Task(
                name=task_name,
                steps=[],
                task_profile=[task_data["description"]],
                agent=[],
                tools=[],
                async_execution=False,
                context=None,
                config=None,
                output_json=None,
                output_pydantic=None,
                output_file=None,
                human_input=False,
                converter_cls=None,
                callback=None
            )
            for task_name, task_data in tasks_dict.items()
        ]