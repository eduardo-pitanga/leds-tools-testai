import json

# Carregue o documento Swagger (pode ser um arquivo JSON ou YAML)
with open('C:/Users/gabri/test_generation_ai/docs/swagger.json', 'r') as f:
    swagger_data = json.load(f)

# Obtenha os endpoints
endpoints = []
for path, methods in swagger_data.get('paths', {}).items():
    for method in methods.keys():
        endpoints.append(f"{method.upper()} {path}")

# Exiba os endpoints
print(*endpoints, sep="\n", file=open("C:/Users/gabri/test_generation_ai/docs/endpoints.txt", "w"))
