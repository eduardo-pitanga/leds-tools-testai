from src.domain.entities.task import Task

class TaskLoader:
    def __init__(self):
        pass

    @staticmethod
    def load_tasks(task_dict: dict, agent=None, context=None, output_file=None) -> Task:
        """
        Carrega uma tarefa a partir de um dicionário fornecido.

        :param task_dict: Dicionário contendo a configuração da tarefa.
        :param agent: Agente responsável pela tarefa.
        :param context: Contexto da tarefa.
        :param output_file: Caminho do arquivo de saída.
        :return: Objeto Task.
        """
        return Task(
            name=task_dict.get("name", "task"),
            steps=task_dict.get("steps", []),
            task_profile=[task_dict["description"]],
            agent=[agent] if agent else [],
            tools=task_dict.get("tools", []),
            async_execution=task_dict.get("async_execution", False),
            context=context,
            config=task_dict.get("config"),
            output_json=task_dict.get("output_json"),
            output_pydantic=task_dict.get("output_pydantic"),
            output_file=output_file,
            human_input=task_dict.get("human_input", False),
            converter_cls=task_dict.get("converter_cls"),
            callback=task_dict.get("callback"),
        )