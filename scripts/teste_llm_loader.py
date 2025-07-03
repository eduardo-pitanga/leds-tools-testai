from src.infrastructure.loaders.llm_loader import LLM_Loader

def test_llm_loader():
    # Parâmetros de teste
    model = "gpt-4"
    temperature = 0.7
    api_key = "test_api_key"

    # Carregar o LLM usando o loader
    llm_instance = LLM_Loader.load_from_params(model=model, temperature=temperature, api_key=api_key)

    # Verificar os atributos do LLM
    assert llm_instance.model == model, f"Expected model {model}, got {llm_instance.model}"
    assert llm_instance.temperature == temperature, f"Expected temperature {temperature}, got {llm_instance.temperature}"
    assert llm_instance.api_key == api_key, f"Expected API key {api_key}, got {llm_instance.api_key}"

    print("All tests passed!")

# Executar o teste
if __name__ == "__main__":
    test_llm_loader()

# linha pra rodar => python -m scripts.teste_llm_loader