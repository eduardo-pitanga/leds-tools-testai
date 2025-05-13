from src.domain.entities.llm import llm

class LLM_Loader:
    @staticmethod
    def load_from_params(model: str, temperature: float, api_key: str) -> llm:
        """
        Carrega a entidade LLM a partir de parâmetros fornecidos.

        :param model: Nome do modelo LLM.
        :param temperature: Temperatura para geração de texto.
        :param api_key: Chave de API para acessar o modelo.
        :return: Instância da entidade llm.
        """
        return llm(
            model=model,
            temperature=temperature,
            api_key=api_key
        )