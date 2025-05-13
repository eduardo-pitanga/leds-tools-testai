from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
from typing import Dict, List
from src.infrastructure.loaders.agent_yaml_loader import AgentLoader 
from src.infrastructure.loaders.llm_loader import LLM_Loader 
from src.infrastructure.loaders.task_yaml_loader import TaskLoader  

load_dotenv()

def crew_gherkin(user_case: str, strings: Dict[str, str]) -> str:
    llm_low_temp: LLM = LLM_Loader.load_from_params()
    llm_high_temp: LLM = LLM_Loader.load_from_params(temperature=0.6)

    agent_loader = AgentLoader()

    agents_dict: Dict[str, str] = strings["agents"]
    tasks_dict: Dict[str, str] = strings["tasks"]

    tasks: List[Task] = []
    agents: List[Agent] = []

    for turn in range(1, 4):
        agents_dict['gherkin_writer']['role'] = agents_dict['gherkin_writer']['role'].format(turn=turn)
        agents_dict['gherkin_reviewer']['role'] = agents_dict['gherkin_reviewer']['role'].format(turn=turn)

        gherkin_writer_agent = agent_loader.load_agents({"gherkin_writer": agents_dict["gherkin_writer"]})[0]
        gherkin_reviewer_agent = agent_loader.load_agents({"gherkin_reviewer": agents_dict["gherkin_reviewer"]})[0]

        tasks_dict["gherkin_code"]["description"] = tasks_dict["gherkin_code"]["description"].format(user_case=user_case)
        task_gherkin_code: Task = TaskLoader().load_tasks({"gherkin_code": tasks_dict["gherkin_code"]})[0]

        tasks_dict["gherkin_review"]["description"] = tasks_dict["gherkin_review"]["description"].format(user_case=user_case)
        task_gherkin_review: Task = TaskLoader().load_tasks({"gherkin_review": tasks_dict["gherkin_review"]})[0]

        agents.append(gherkin_writer_agent)
        agents.append(gherkin_reviewer_agent)
        tasks.append(task_gherkin_code)
        tasks.append(task_gherkin_review)

    manager = agent_loader.load_agents({"manager_gherkin": agents_dict["manager_gherkin"]})[0]

    final_task: Task = TaskLoader().load_tasks({"manager_gherkin_task": tasks_dict["manager_gherkin_task"]})[0]

    
    crew: Crew = Crew(
        agents=agents + [manager],
        tasks=tasks + [final_task],
        max_rpm=10,
        output_log_file="crew_log.txt",
        manager_llm=llm_low_temp,
        process=Process.sequential,
        verbose=True
    )

    resultado = crew.kickoff()
    return resultado.raw