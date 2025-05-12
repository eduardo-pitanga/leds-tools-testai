class llm:
    def __init__(self, model: str, temperature: float, api_key: str):
        self.model = model
        self.temperature = temperature
        self.api_key = api_key

    def __repr__(self):
        return f"LLM(model={self.model}, temperature={self.temperature}, api_key={self.api_key})"