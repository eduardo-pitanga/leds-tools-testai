import yaml
import os
from src.domain.entities.agent import Agent
from src.domain.entities.llm import llm

class AgentYAMLLoader():
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_agents(self) -> list[Agent]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return [
            Agent(
                name=agent_name,
                role=agent_data["role"],
                goal=agent_data["goal"],
                backstory=agent_data["backstory"],
                llm=llm(model="gpt-4", temperature=0.0, api_key=(os.getenv("GOOGLE_API_KEY"))),
                config=None,
                cache=False,
                verbose=False,
                max_rpm=10,
                allow_delegation=False,
                tools=[],
                max_iter=100,
                function_calling_llm=None,
                max_execution_time=3600,
                step_callback=None,
                system_template="",
                prompt_template="",
                response_template="",
                allow_code_execution=False,
                max_retry_limit=3,
                use_system_prompt=True,
                respect_context_window=True,
                code_execution_mode="default"
            )
            for agent_name, agent_data in data.items()
        ]