from src.infrastructure.loaders.agent_yaml_loader import AgentLoader

def main():
    # Dicionário com os dados dos agentes
    agents_dict = {
        "gherkin_writer": {
            "role": "Gherkin Writer - Turn {turn}",
            "goal": "Write Gherkin scenarios",
            "backstory": "An AI specialized in writing Gherkin scenarios."
        },
        "gherkin_reviewer": {
            "role": "Gherkin Reviewer - Turn {turn}",
            "goal": "Review Gherkin scenarios",
            "backstory": "An AI specialized in reviewing Gherkin scenarios."
        },
        "manager_gherkin": {
            "role": "Manager",
            "goal": "Oversee the Gherkin process",
            "backstory": "An AI manager for Gherkin tasks."
        }
    }

    # Cria uma instância do loader
    loader = AgentLoader()

    # Carrega os agentes a partir do dicionário
    agents = loader.load_agents(agents_dict)

    # Exibe os agentes carregados
    for agent in agents:
        print(agent)

if __name__ == "__main__":
    main()


## linha pra rodar => python -m scripts.teste_agent_loader