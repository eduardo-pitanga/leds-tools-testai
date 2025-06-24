import pytest
from src.infrastructure.loaders.agent_loader import AgentLoader
from src.domain.entities.agent import Agent
from src.domain.entities.llm import llm

def test_agent_loader_valid():
    profile = {
        "name": "MyAgent",
        "role": "R",
        "goal": "G",
        "backstory": "B"
    }
    fake_llm = llm("m", 0.1, "k")
    agent = AgentLoader.load_agents(profile, fake_llm)

    # Agora retornamos um único Agent, não lista
    assert isinstance(agent, Agent)
    assert agent.role == "R"
    assert agent.llm is fake_llm

def test_agent_loader_missing_field():
    fake_llm = llm("m", 0.1, "k")
    # omitindo 'backstory' — deve lançar KeyError
    with pytest.raises(KeyError):
        AgentLoader.load_agents({"role": "R", "goal": "G"}, fake_llm)
