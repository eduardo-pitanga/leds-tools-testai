from src.domain.entities.llm import llm

class Agent:
    def __init__(self, name: str, role: str, goal: str, backstory: str, llm: llm, config: any,
                 cache: bool, verbose: bool, max_rpm: int,
                 allow_delegation: bool, tools: list, max_iter: int,
                 function_calling_llm: llm, max_execution_time: int,
                 step_callback: callable, system_template: str,
                 prompt_template: str, response_template: str,
                 allow_code_execution: bool, max_retry_limit: int,
                 use_system_prompt: bool, respect_context_window: bool,
                 code_execution_mode: str):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm = llm
        self.config = config
        self.cache = cache
        self.verbose = verbose
        self.max_rpm = max_rpm
        self.allow_delegation = allow_delegation
        self.tools = tools
        self.max_iter = max_iter
        self.function_calling_llm = function_calling_llm
        self.max_execution_time = max_execution_time
        self.step_callback = step_callback
        self.system_template = system_template
        self.prompt_template = prompt_template
        self.response_template = response_template
        self.allow_code_execution = allow_code_execution
        self.max_retry_limit = max_retry_limit
        self.use_system_prompt = use_system_prompt
        self.respect_context_window = respect_context_window
        self.code_execution_mode = code_execution_mode

    def __repr__(self):
        return f"<Agent name={self.name}, role={self.role}, goal={self.goal}>, backstory={self.backstory}>, LLM={self.llm}, config={self.config}, cache={self.cache}, verbose={self.verbose}, max_rpm={self.max_rpm}, allow_delegation={self.allow_delegation}, tools={self.tools}, max_iter={self.max_iter}, function_calling_llm={self.function_calling_llm}, max_execution_time={self.max_execution_time}, step_callback={self.step_callback}, system_template={self.system_template}, prompt_template={self.prompt_template}, response_template={self.response_template}, allow_code_execution={self.allow_code_execution}, max_retry_limit={self.max_retry_limit}, use_system_prompt={self.use_system_prompt}, respect_context_window={self.respect_context_window}, code_execution_mode={self.code_execution_mode}>"