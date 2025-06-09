from src.infrastructure.loaders.task_yaml_loader import TaskLoader

def main():
    # Dicionário com os dados das tarefas
    tasks_dict = {
        "gherkin_code": {
            "description": "Generate Gherkin code for the user case: {user_case}"
        },
        "gherkin_review": {
            "description": "Review the Gherkin code for the user case: {user_case}"
        },
        "manager_gherkin_task": {
            "description": "Manage the Gherkin process for the user case: {user_case}"
        }
    }

    # Cria uma instância do loader
    loader = TaskLoader()

    # Carrega as tarefas a partir do dicionário
    tasks = loader.load_tasks(tasks_dict)

    # Exibe as tarefas carregadas
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()


## linha pra rodar => python -m scripts.teste_task_loader