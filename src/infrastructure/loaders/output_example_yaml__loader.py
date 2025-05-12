import yaml
from typing import Dict

def load_output_examples(file_path: str = "src/config/output_examples.yaml") -> Dict[str, str]:
    """
    Carrega os exemplos de saída do arquivo YAML.

    Args:
        file_path (str): Caminho para o arquivo output_examples.yaml.

    Returns:
        Dict[str, str]: Um dicionário contendo os exemplos de saída.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            output_examples = yaml.safe_load(file)
        return output_examples
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Erro ao carregar o arquivo YAML: {e}")

# Exemplo de uso
if __name__ == "__main__":
    examples = load_output_examples()
    print(examples)