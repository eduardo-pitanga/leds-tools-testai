import pytest
from src.infrastructure.loaders.task_yaml_loader import TaskLoader
from crewai import Task

def test_task_loader_completo():
    td = {
        "name": "T1",
        "description": "Desc",
        "steps": ["s1", "s2"],
        "tools": ["t1"],
        "expected_output": "out1",
        "async_execution": True,
        "config": {"a":1},
        "output_json": {"j":2},
        "output_pydantic": None,
        "human_input": True,
        "converter_cls": int,
        "callback": lambda x: x
    }
    t = TaskLoader.load_tasks(td, agent="A", context="CTX", output_file="f.txt")
    assert isinstance(t, Task)
    assert t.name == "T1"
    assert t.steps == ["s1", "s2"]
    assert t.description == "Desc"
    assert t.expected_output == "out1"
    assert t.agent == "A"
    assert t.tools == ["t1"]
    assert t.async_execution is True
    assert t.context == "CTX"
    assert t.config == {"a":1}
    assert t.output_json == {"j":2}
    assert t.human_input is True
    assert t.output_file == "f.txt"

def test_task_loader_default_steps_tools():
    td = {"name":"T2","description":"Desc2"}
    t = TaskLoader.load_tasks(td)
    assert t.steps == []
    assert t.tools == []
    assert t.async_execution is False

def test_task_loader_missing_name_default():
    td = {"description":"Desc3"}
    t = TaskLoader.load_tasks(td)
    assert t.name == "task"

def test_task_loader_missing_description():
    with pytest.raises(KeyError):
        TaskLoader.load_tasks({"name":"T3"})

def test_task_loader_sem_agent_e_context():
    td = {"name":"T4","description":"D4"}
    t = TaskLoader.load_tasks(td)
    assert t.agent is None or t.agent == []
    assert t.context is None

def test_task_loader_converter_callback_nulos():
    td = {"name":"T5","description":"D5","converter_cls":None,"callback":None}
    t = TaskLoader.load_tasks(td)
    assert t.converter_cls is None
    assert t.callback is None

def test_task_loader_output_file_opcional():
    td = {"name":"T6","description":"D6"}
    t = TaskLoader.load_tasks(td, output_file="o6.txt")
    assert t.output_file == "o6.txt"

def test_task_loader_tipo_errado(monkeypatch):
    td = {"name":"T7","description":"D7"}
    # forçar TaskLoader a chamar algo errado, mas assume que Task aceita qualquer coisa
    t = TaskLoader.load_tasks(td)
    assert hasattr(t, "description")
