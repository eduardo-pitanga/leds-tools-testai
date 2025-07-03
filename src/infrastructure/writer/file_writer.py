class FileWriter:
    def save(self, path: str, content: str):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)