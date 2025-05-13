import os
from src.domain.entities.llm import llm

class LLM_Loader:
    @staticmethod
    def load_from_params(
        model: str = None,
        temperature: float = None,
        api_key: str = None
    ) -> llm:
        """
        Carrega a entidade LLM a partir de parâmetros fornecidos ou das variáveis de ambiente.

        :param model: Nome do modelo LLM.
        :param temperature: Temperatura para geração de texto.
        :param api_key: Chave de API para acessar o modelo.
        :return: Instância da entidade llm.
        """
        model = model or os.getenv("LLM_MODEL", "gemini/gemini-1.5-flash")
        temperature = temperature if temperature is not None else float(os.getenv("LLM_TEMPERATURE", 0.0))
        api_key = api_key or os.getenv("GOOGLE_API_KEY")

        return llm(
            model=model,
            temperature=temperature,
            api_key=api_key
        )