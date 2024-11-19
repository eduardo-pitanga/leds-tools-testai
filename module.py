from crewai import LLM, Agent, Task
import os
from pydantic import BaseModel
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class AgentProfile(BaseModel):
    role: str
    goal: str
    backstory: str

def init_llm(
        model: str ='gemini/gemini-1.5-flash',
        temp: float = 0.0,
        key: str = os.getenv("GOOGLE_API_KEY")
) -> LLM:    
    return LLM(
        model=model,
        temperature=temp,
        api_key=key,
    )

def init_agent(
    agent_profile: AgentProfile,
    llm: LLM,
    config = None,
    cache = True,
    verbose = False,
    max_rpm = None,
    allow_delegation = False,
    tools = [],
    max_iter = 25,
    function_calling_llm = None,
    max_execution_time = None,
    step_callback = None,
    system_template = None,
    prompt_template = None,
    response_template = None,
    allow_code_execution = False,
    max_retry_limit = 2,
    use_system_prompt = True,
    respect_context_window = True,
    code_execution_mode = 'safe'
) -> Agent:
    return Agent(
        role = agent_profile["role"],
        goal = agent_profile["goal"],
        backstory = agent_profile["backstory"],
        llm = llm,
        config = config,
        cache = cache,
        verbose = verbose,
        max_rpm = max_rpm,
        allow_delegation = allow_delegation,
        tools = tools,
        max_iter = max_iter,
        function_calling_llm = function_calling_llm,
        max_execution_time = max_execution_time,
        step_callback = step_callback,
        system_template = system_template,
        prompt_template = prompt_template,
        response_template = response_template,
        allow_code_execution = allow_code_execution,
        max_retry_limit = max_retry_limit,
        use_system_prompt = use_system_prompt,
        respect_context_window = respect_context_window,
        code_execution_mode = code_execution_mode
    )

def init_task(
    task_profile,
    agent,
    tools = [],
    async_execution = False,
    context = None,
    config = None,
    output_json = None,
    output_pydantic = None,
    output_file = "",
    human_input = False,
    converter_cls = None,
    callback = None
) -> Task:
    return Task(
        description = task_profile["description"],
        expected_output = task_profile["expected_output"],
        agent = agent,
        tools = tools,
        async_execution = async_execution,
        context = context,
        config = config,
        output_json = output_json,
        output_pydantic = output_pydantic,
        output_file = output_file,
        human_input = human_input,
        converter_cls = converter_cls,
        callback = callback
    )