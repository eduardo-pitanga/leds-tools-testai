class Task:
    def __init__(self, name: str, description: str, expected_output: str, output_example: str | None = None):
        self.name = name
        self.description = description
        self.expected_output = expected_output
        self.output_example = output_example

    def __repr__(self):
        return f"<Task name={self.name}, has_example={self.output_example is not None}>"