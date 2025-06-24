import pytest
from src.infrastructure.loaders.task_yaml_loader import TaskLoader
from src.domain.entities.task import Task

def test_task_loader_valid():
    td = {"description":"d","name":"T","steps":["s1"],"tools":["t"]}
    t = TaskLoader.load_tasks(td, agent="A", context="C", output_file="o.txt")
    assert isinstance(t, Task)
    assert t.name == "T"
    assert t.steps == ["s1"]
    assert t.context == "C"
    assert t.output_file == "o.txt"

def test_task_loader_missing_description():
    with pytest.raises(KeyError):
        TaskLoader.load_tasks({"name":"T"}, agent=None, context=None)