from crewai import Agent, Task, Crew, Process, LLM
#import os
from dotenv import load_dotenv
#import json
from typing import Dict, List
from module import init_task, init_agent, init_llm

load_dotenv()

def crew_gherkin(user_case: str, strings: Dict[str, str]) -> str:
    
    llm_low_temp: LLM = init_llm()
    llm_high_temp: LLM = init_llm(temp=0.6)

    agents_dict: Dict[str, str] = strings["agents"]
    tasks_dict: Dict[str, str] = strings["tasks"]
    
    tasks: List[Task] = []
    agents: List[Agent] = []

    for turn in range(1,4):
        agents_dict['gherkin_writer']['role'] = agents_dict['gherkin_writer']['role'].format(turn=turn)
        gherkin_writer_agent: Agent = init_agent(agents_dict["gherkin_writer"], llm_high_temp)

        agents_dict['gherkin_reviewer']['role'] = agents_dict['gherkin_reviewer']['role'].format(turn=turn)
        gherkin_reviewer_agent: Agent = init_agent(agents_dict["gherkin_reviewer"], llm_low_temp)

        tasks_dict["gherkin_code"]["description"] = tasks_dict["gherkin_code"]["description"].format(user_case=user_case)
        task_gherkin_code: Task = init_task(
            tasks_dict["gherkin_code"],
            gherkin_writer_agent,
            #output_file=f"etapas_geracao/rodada_{turn}.cs"
        )

        tasks_dict["gherkin_review"]["description"] = tasks_dict["gherkin_review"]["description"].format(user_case=user_case)
        task_gherkin_review: Task = init_task(
            tasks_dict["gherkin_review"],
            gherkin_reviewer_agent,
            context=[task_gherkin_code],
            #output_file=f"etapas_geracao/revisao_{turn}.cs"
        )
        
        agents.append(gherkin_writer_agent)
        agents.append(gherkin_reviewer_agent)

        tasks.append(task_gherkin_code)
        tasks.append(task_gherkin_review)

    manager: Agent = init_agent(agents_dict["manager_gherkin"], llm_low_temp)
    final_task: Task = init_task(
        tasks_dict["manager_gherkin_task"],
        output_file="features/ListarModalidadeFeature.feature",
        agent=manager,
        context=tasks[1::2],
    )

    crew: Crew = Crew(
        agents=agents+[manager],
        tasks=tasks+[final_task],
        max_rpm=10,
        output_log_file="crew_log.txt",
        #manager_agent=manager_agent,
        manager_llm=llm_low_temp,
        process=Process.sequential,
        verbose=True
        
    )
    
    resultado = crew.kickoff()
    return resultado.raw