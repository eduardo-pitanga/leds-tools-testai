import json

def extract_endpoints(swagger_path: str) -> list[str]:
    with open(swagger_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    endpoints = []
    for path, methods in data.get('paths', {}).items():
        for method in methods.keys():
            endpoints.append(f"{method.upper()} {path}")
    return endpoints