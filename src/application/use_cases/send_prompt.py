import requests
import strip_markdown

def send_to_debate_api(payload: dict) -> str:
    result = requests.post("http://127.0.0.1:8080/gherkin", json=payload)
    return strip_markdown.strip_markdown(result.content.decode("utf-8"))

def send_to_sequencial_api(payload: dict) -> str:
    result = requests.post("http://127.0.0.1:8000/gherkin", json=payload)
    return strip_markdown.strip_markdown(result.content.decode("utf-8"))