from src.infrastructure.loaders.task_yaml_loader import TaskYAMLLoader

def main():
    # Caminho para o arquivo YAML
    file_path = "c:\\Users\\teixe\\Desktop\\testai\\leds-tools-testai\\src\\config\\tasks.yaml"
    
    # Cria uma instância do loader
    loader = TaskYAMLLoader(file_path)
    
    # Carrega as tarefas
    tasks = loader.load_tasks()
    
    # Exibe as tarefas carregadas
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()