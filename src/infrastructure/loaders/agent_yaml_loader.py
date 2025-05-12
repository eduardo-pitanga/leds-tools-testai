import yaml
from domain.entities.agent import Agent
from application.interfaces.agent_repository import AgentRepository

class AgentYAMLLoader(AgentRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_agents(self) -> list[Agent]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return [Agent(**agent_data) for agent_data in data.get("agents", [])]
