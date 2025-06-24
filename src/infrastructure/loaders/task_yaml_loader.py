from src.domain.entities.task import Task

class TaskLoader:
    @staticmethod
    def load_tasks(task_dict: dict, agent=None, context=None, output_file=None) -> Task:
        task_kwargs = {
            "name": task_dict.get("name", "task"),
            "steps": task_dict.get("steps", []),
            "task_profile": task_dict["description"],  
            "agent": agent,
            "tools": task_dict.get("tools", []),
            "async_execution": task_dict.get("async_execution", False),
            "context": context,
            "config": task_dict.get("config"),
            "output_json": task_dict.get("output_json"),
            "output_pydantic": task_dict.get("output_pydantic"),
            "output_file": output_file,
            "human_input": task_dict.get("human_input", False),
            "converter_cls": task_dict.get("converter_cls"),
            "callback": task_dict.get("callback"),
        }
        
        task_kwargs = {k: v for k, v in task_kwargs.items() if v is not None}
        return Task(**task_kwargs)