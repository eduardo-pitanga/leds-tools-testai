import pytest
from src.infrastructure.loaders.llm_loader import LLM_Loader
from src.domain.entities.llm import llm

def test_llm_loader_default_env(monkeypatch):
    # Se não passar nada, deve ler do env ou usar defaults
    monkeypatch.setenv("LLM_MODEL", "env-model")
    monkeypatch.setenv("LLM_TEMPERATURE", "0.4")
    monkeypatch.setenv("GOOGLE_API_KEY", "env-key")
    inst = LLM_Loader.load_from_params()
    assert isinstance(inst, llm)
    assert inst.model == "env-model"
    assert abs(inst.temp - 0.4) < 1e-6
    assert inst.api_key == "env-key"

def test_llm_loader_with_params():
    inst = LLM_Loader.load_from_params(model="m", temp=0.7, api_key="k")
    assert isinstance(inst, llm)
    assert inst.model == "m"
    assert inst.temp == 0.7
    assert inst.api_key == "k"

def test_llm_loader_bad_temperature():
    with pytest.raises(ValueError):
        # temp deve ser float convertível
        LLM_Loader.load_from_params(temp="not-a-number")