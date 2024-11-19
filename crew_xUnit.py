from crewai import Process, LLM, Task, Agent, Crew
from typing import Dict, List
import yaml
from module import init_task, init_agent, init_llm
from pprint import pprint

llm_high_temp: LLM = init_llm(temp=0.8)
llm_low_temp: LLM = init_llm()

def crew_gherkin(user_case: str, strings: Dict[str, str]) -> str:
    
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
            output_file=f"etapas_geracao/rodada_{turn}.cs"
        )

        tasks_dict["gherkin_review"]["description"] = tasks_dict["gherkin_review"]["description"].format(user_case=user_case)
        task_gherkin_review: Task = init_task(
            tasks_dict["gherkin_review"],
            gherkin_reviewer_agent,
            context=[task_gherkin_code],
            output_file=f"etapas_geracao/revisao_{turn}.cs"
        )
        
        agents.append(gherkin_writer_agent)
        agents.append(gherkin_reviewer_agent)

        tasks.append(task_gherkin_code)
        tasks.append(task_gherkin_review)


    manager: Agent = init_agent(agents["manager_gherkin"], llm_low_temp)

    final_task: Task = init_task(
        tasks_dict["manager_gherkin_task"],
        output_file="etapas_geracao/final/RequisitoBolsaFeature.cs",
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

def crew_xunit_paralelo(feature: str, string: Dict[str, str]) -> str:
    agents_dict: Dict[str, str] = strings["agents"]
    tasks_dict: Dict[str, str] = strings["tasks"]
    
    #binding dos features na descricao e concatenacao dos outputs de exemplo
    tasks_dict["xunit_code_proposal"]["description"] = tasks_dict["xunit_code_proposal"]["description"].format(feature=feature) + tasks_dict["xunit_code_proposal"]["output_example"]
    tasks_dict["xunit_review"]["description"] = tasks_dict["xunit_review"]["description"].format(feature=feature) + tasks_dict["xunit_review"]["output_example"]
    tasks_dict["manager_xunit_task"]["description"] = tasks_dict["manager_xunit_task"]["description"].format(feature=feature) + tasks_dict["manager_xunit_task"]["output_example"]
    
    tasks: List[Task] = []
    agents: List[Agent] = []

    gemini_llm: LLM = init_llm(temp=0.2)

    for turn in range(1,4):
        print(turn)
        csharp_xunit_writer_agent: Agent = init_agent(agents_dict["csharp_xunit_writer"], gemini_llm)

        xunit_code_proposal: Task = init_task(
            tasks_dict["xunit_code_proposal"],
            agent=csharp_xunit_writer_agent,
            output_file=f"VersionarModalidadeTest/rodada_{turn}.cs"
            )
                
        agents.append(csharp_xunit_writer_agent)
        tasks.append(xunit_code_proposal)

        xunit_code_reviewer_agent: Agent = init_agent(agents_dict["xunit_code_reviewer_agent"], gemini_llm)
        
        xunit_code_review_task: Task = init_task(
            tasks_dict["xunit_review"],
            xunit_code_reviewer_agent,
            context=[tasks[-1]],
            output_file=f"VersionarModalidadeTest/revisao_{turn}.cs"
            )
        
        agents.append(xunit_code_reviewer_agent)
        tasks.append(xunit_code_review_task)
    
    manager: Agent = init_agent(agents_dict["result_analysis_manager"], gemini_llm)

    manager_task: Task = init_task(tasks_dict["manager_xunit_task"],
                                   manager, context=tasks[1::2],
                                   output_file="VersionarModalidadeTest/final/VersionarModalidadeFeature.cs")

    agents.append(manager)
    tasks.append(manager_task)

    crew: Crew = Crew(
        agents=agents,
        tasks=tasks,
        max_rpm=10,
        output_log_file="crew_log.txt",
        #manager_agent=manager_agent,
        manager_llm=llm_low_temp,
        process=Process.sequential,
        verbose=True
    )

    resultado = crew.kickoff()
    return resultado.raw


def crew_xunit_debate(feature: str, strings: Dict[str, str]) -> str:
    
    agents_dict: Dict[str, str] = strings["agents"]
    tasks_dict: Dict[str, str] = strings["tasks"]
    
    tasks: List[Task] = []
    agents: List[Agent] = []

    gemini_llm: LLM = init_llm(temp=0.2)

    csharp_xunit_writer_agent: Agent = init_agent(agents_dict["csharp_xunit_writer"], gemini_llm)

    tasks_dict["xunit_code_proposal"]["description"] = tasks_dict["xunit_code_proposal"]["description"].format(feature=feature)
    xunit_code_proposal: Task = init_task(tasks_dict["xunit_code_proposal"], agent=csharp_xunit_writer_agent)
    
    agents.append(csharp_xunit_writer_agent)
    tasks.append(xunit_code_proposal)

    for i in range(1,4):
        xunit_solution_discussion_agent: Agent = init_agent(agents_dict["xunit_solution_discussion"], gemini_llm)

        tasks_dict["debate"]["description"] = tasks_dict["debate"]["description"].format(feature=feature)
        debate: Task = init_task(tasks_dict["debate"], agent=xunit_solution_discussion_agent)

        agents.append(xunit_solution_discussion_agent)
        tasks.append(debate)
    
    result_analysis_manager_agent: Agent = init_agent(agents_dict["result_analysis_manager"], llm=gemini_llm)

    tasks_dict["manager_xunit_task"]["description"] = tasks_dict["manager_xunit_task"]["description"].format(feature=feature)
    manager_xunit_task: Task = init_task(
        tasks_dict["manager_xunit_task"],
        output_file=f"modalidade_bolsa_crew.cs",
        agent=result_analysis_manager_agent,
        context=[tasks[-1]],
    )

    crew: Crew = Crew(
        agents=agents + [result_analysis_manager_agent],
        tasks=tasks + [manager_xunit_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff().raw
    
with open("VersaoModalidadeFeature.feature", encoding='utf-8') as file:
    feature = file.read()

with open("strings_ingles.yaml", encoding="utf-8") as file:
    strings: Dict[str, str] = yaml.safe_load(file)

gherkin = crew_xunit_paralelo(feature, strings)