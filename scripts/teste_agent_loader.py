from src.infrastructure.loaders.agent_yaml_loader import AgentYAMLLoader

def main():
    # Caminho para o arquivo YAML
    file_path = "c:\\Users\\teixe\\Desktop\\testai\\leds-tools-testai\\src\\config\\agents.yaml"
    
    # Cria uma instância do loader
    loader = AgentYAMLLoader(file_path)
    
    # Carrega os agentes
    agents = loader.load_agents()
    
    # Exibe os agentes carregados
    for agent in agents:
        print(agent)

if __name__ == "__main__":
    main()


## linha pra rodar => python -m scripts.teste_agent_loader