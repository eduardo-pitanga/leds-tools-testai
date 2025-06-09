import os
from src.domain.entities.agent import Agent
from src.infrastructure.loaders.llm_loader import LLM_Loader
from src.domain.entities.llm import llm

class AgentLoader():
    
    def load_agents(agent_dict: dict, llm: llm) -> list[Agent]:
        """
        Load agents from a dictionary instead of a YAML file.

        :param agents_dict: Dictionary containing agent configurations.
        :return: List of Agent objects.
        """
        return [
            Agent(
                name=agent_dict.get("name", "agent"),
                role=agent_dict["role"],
                goal=agent_dict["goal"],
                backstory=agent_dict["backstory"],
                llm=llm,
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
            #for agent_name, agent_data in agents_dict.items()
        ]