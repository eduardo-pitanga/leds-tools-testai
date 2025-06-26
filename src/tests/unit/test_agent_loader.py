import pytest
from src.infrastructure.loaders.agent_yaml_loader import AgentLoader
from crewai import Agent, LLM

def test_carrega_agente_completo():
    perfil = {"name":"A1","role":"R1","goal":"G1","backstory":"B1"}
    llm_fake = LLM(model="m", temperature=0.1, api_key="k")
    agente = AgentLoader.load_agents(perfil, llm_fake)
    assert isinstance(agente, Agent)
    assert agente.name == "A1"
    assert agente.role == "R1"
    assert agente.goal == "G1"
    assert agente.backstory == "B1"
    assert agente.llm is llm_fake

def test_carrega_agente_sem_name_usando_default():
    perfil = {"role":"R2","goal":"G2","backstory":"B2"}
    llm_fake = LLM(model="m", temperature=0.2, api_key="k2")
    agente = AgentLoader.load_agents(perfil, llm_fake)
    assert agente.name == "agent"

def test_falha_sem_role():
    perfil = {"name":"A3","goal":"G3","backstory":"B3"}
    with pytest.raises(KeyError):
        AgentLoader.load_agents(perfil, LLM(model="x", temperature=0, api_key="k"))

def test_falha_sem_goal():
    perfil = {"name":"A4","role":"R4","backstory":"B4"}
    with pytest.raises(KeyError):
        AgentLoader.load_agents(perfil, LLM(model="x", temperature=0, api_key="k"))

def test_falha_sem_backstory():
    perfil = {"name":"A5","role":"R5","goal":"G5"}
    with pytest.raises(KeyError):
        AgentLoader.load_agents(perfil, LLM(model="x", temperature=0, api_key="k"))

def test_tipo_llm_errado():
    perfil = {"name":"A6","role":"R6","goal":"G6","backstory":"B6"}
    with pytest.raises(AttributeError):
        # passar algo que não seja LLM
        AgentLoader.load_agents(perfil, llm="nao-é-llm")  # deve acessar .model e falhar

def test_retorno_nao_é_lista():
    perfil = {"name":"A7","role":"R7","goal":"G7","backstory":"B7"}
    agente = AgentLoader.load_agents(perfil, LLM(model="m", temperature=0.3, api_key="k"))
    assert not isinstance(agente, list)

def test_objeto_agent_válido():
    perfil = {"name":"A8","role":"R8","goal":"G8","backstory":"B8"}
    llm_fake = LLM(model="m", temperature=0.4, api_key="k4")
    agente = AgentLoader.load_agents(perfil, llm_fake)
    # checa alguns atributos internos padrão
    assert agente.cache is False
    assert agente.verbose is False
    assert agente.max_rpm == 10
