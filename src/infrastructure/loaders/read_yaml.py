from yaml import safe_load
from typing import List, Dict, Tuple

def read_yaml_strings() -> Tuple[Dict[str, str], Dict[str, str]]:
    with open("src/config/agents.yaml", encoding="utf-8") as file:
        agents_yaml = safe_load(file)

    with open("src/config/tasks.yaml", encoding="utf-8") as file:
        tasks_yaml = safe_load(file)
    
    with open("src/config/output_examples.yaml") as file:
        output_yaml = safe_load(file)

    return agents_yaml, tasks_yaml, output_yaml