from infrastructure.utils.swagger_parser import extract_endpoints

swagger_path = "docs/swagger.json"
endpoints = extract_endpoints(swagger_path)

with open("docs/endpoints.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(endpoints))
