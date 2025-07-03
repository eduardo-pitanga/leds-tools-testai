import pytest
from src.infrastructure.loaders.agent_yaml_loader import AgentLoader
from src.domain.entities.agent import Agent
from src.domain.entities.llm import llm

def test_agent_loader_valid():
    profile = {"role":"R","goal":"G","backstory":"B","name":"N"}
    fake_llm = llm("m", 0.1, "k")
    agents = AgentLoader.load_agents(profile, fake_llm)
    assert isinstance(agents, list)
    assert len(agents) == 1
    a = agents[0]
    assert isinstance(a, Agent)
    assert a.role == "R"
    assert a.llm is fake_llm

def test_agent_loader_missing_field():
    fake_llm = llm("m",0.1,"k")
    with pytest.raises(KeyError):
        # backstory ausente
        AgentLoader.load_agents({"role":"R","goal":"G"}, fake_llm)