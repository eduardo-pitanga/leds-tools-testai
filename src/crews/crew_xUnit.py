from crewai import Process, LLM, Task, Agent, Crew
from crewai_tools import FileReadTool, DirectoryReadTool
from typing import Dict, List
from module import init_task, init_agent, init_llm, read_yaml_strings
import asyncio
import time

llm_high_temp: LLM = init_llm(temp=0.8)
llm_low_temp: LLM = init_llm()

agents_dict, tasks_dict, outputs_dict = read_yaml_strings()

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


def info_gatherer_crew(feature: str) -> tuple[str, str]:
    agent_api_finder = Agent(
    role="API Path Finder",
    goal="Identify and extract API URL paths from Swagger documents to streamline API integration and documentation.",
    backstory="A meticulous and detail-oriented digital assistant, trained extensively in API documentation and Swagger standards. Equipped with a keen eye for structure and patterns, the agent thrives in simplifying complex API schemas for developers.",
    llm=llm_low_temp,
    verbose=True,
    tools=[FileReadTool()],
    )

    agent_file_searcher = Agent(
    role="File Search Specialist",
    goal="Locate a specific file within a given directory and its subdirectories, ensuring efficient file retrieval for various tasks.",
    backstory="A diligent and organized assistant, fine-tuned for file system navigation and pattern matching. With a background in file management and search optimization, this agent excels at quickly identifying files based on name, type, or content.",
    llm=llm_low_temp,
    tools=[DirectoryReadTool(), FileReadTool()]
    )

    dto_file_find = Task(
        description=f"{feature}"
        """At the path C:/Users/gabri/leds-conectafapes-backend-admin/src/ConectaFapes/ConectaFapes.Application/DTOs
        Find the dto request file and response file for the given feature,
        the open the file and read it content
        """,
        expected_output="The dto response and request class code",
        agent=agent_file_searcher,
        async_execution=True
    )


    api_url_find = Task(
        description=f"{feature}"
        """
        Read the file at C:/Users/gabri/crew2/endpoints.txt
        Use the tool to search for the api url for the given Feature;
        The api_url has the feature title all in lower case;
        You should look not only for the exact correspondence, but also for similars. For example, if the feature title in lowercase is versaomodalidade, you should also consider versaomodalidadebolsa
        """,
        expected_output="Only the complete url path requested and the respective methods",
        agent=agent_api_finder,
    )

    crew = Crew(
        agents=[agent_api_finder, agent_file_searcher],
        tasks=[dto_file_find, api_url_find],
        verbose=True,
        process=Process.sequential
    )

    crew.kickoff()

    print(api_url_find.output.raw, file=open("api_url.txt", "w"))
    print(dto_file_find.output.raw, file=open("dto_code.txt", "w"))

    return dto_file_find.output.raw, api_url_find.output.raw

def crew_xunit_generation(feature: str, api_url, dto_code) -> Crew:
    gemini_llm: LLM = init_llm(temp=0.2)
    agents: list[Agent] = []
    tasks: list[Task] = []

    #bind das features e concantenacao com o output de exemplo
    tasks_dict["xunit_code_proposal"]["description"] = \
        tasks_dict["xunit_code_proposal"]["description"].format(feature=feature) + \
        "The DTO class you should use is: " + dto_code + "\n" + \
        "The url for this feature is " + api_url + "\n" +\
        outputs_dict[tasks_dict["xunit_code_proposal"]["output_example"]]
    
    print(tasks_dict["xunit_code_proposal"]["description"], file=open("xunit_code_proposal_desc.txt", "w"))

    tasks_dict["xunit_review"]["description"] = \
        tasks_dict["xunit_review"]["description"].format(feature=feature) + \
        outputs_dict[tasks_dict["xunit_review"]["output_example"]]
    
    csharp_xunit_writer_agent: Agent = init_agent(agents_dict["csharp_xunit_writer"], gemini_llm)
    xunit_code_proposal: Task = init_task(
        tasks_dict["xunit_code_proposal"],
        agent=csharp_xunit_writer_agent,
        #tools=[]
        #output_file=f"VersionarModalidadeTestImproved/rodada_{turn}.cs",
        #context=[dto_file_find, api_url_find],
        )
            
    agents.append(csharp_xunit_writer_agent)
    tasks.append(xunit_code_proposal)

    xunit_code_reviewer_agent: Agent = init_agent(agents_dict["xunit_code_reviewer_agent"], gemini_llm)
    xunit_code_review_task: Task = init_task(
        tasks_dict["xunit_review"],
        xunit_code_reviewer_agent,
        context=[xunit_code_proposal],
        #output_file=f"VersionarModalidadeTestImproved/revisao_{turn}.cs"
        )
    
    agents.append(xunit_code_reviewer_agent)
    tasks.append(xunit_code_review_task)

    return Crew(
        agents=agents,
        tasks=tasks,
        max_rpm=10,
        output_log_file="crew_log.txt",
        #manager_agent=manager_agent,
        manager_llm=llm_low_temp,
        process=Process.sequential,
        verbose=True
        )

def manager_crew(reviews: tuple[str]) -> None:
    tasks_dict["manager_xunit_task"]["description"] = \
        tasks_dict["manager_xunit_task"]["description"].format(reviews[0], reviews[1], reviews[2]) + \
        outputs_dict[tasks_dict["manager_xunit_task"]["output_example"]]
    
    print(tasks_dict["manager_xunit_task"]["description"], file=open("manager_xunit_task_desc.txt", "w"))

    manager: Agent = init_agent(agents_dict["result_analysis_manager"], llm_low_temp)
    manager_task: Task = init_task(
        tasks_dict["manager_xunit_task"],
        manager, 
        output_file="VersionarModalidadeStepAI.cs"
        )

    crew = Crew(
        agents=[manager],
        tasks=[manager_task],
        process=Process.sequential
    )

    return crew.kickoff()


async def xunit_generation(feature):
    dto_code, api_url = info_gatherer_crew(feature)
    crew_xunit: Crew = crew_xunit_generation(feature, api_url, dto_code)
    result1 = crew_xunit.kickoff_async()
    result2 = crew_xunit.kickoff_async()
    result3 = crew_xunit.kickoff_async()

    results = await asyncio.gather(result1, result2, result3)
    return manager_crew(results)


with open("src/features/VersaoModalidadeFeature.feature") as file:
    feature = file.read()
    start_time = time.time()
    asyncio.run(xunit_generation(feature))
    end_time = time.time()
    print(f"Tempo de execução: {end_time-start_time}")
    #crew_xunit_paralelo(feature)
