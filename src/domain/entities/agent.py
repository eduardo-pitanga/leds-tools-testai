class Agent:
    def __init__(self, name: str, role: str, goal: str, backstory: str):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory

    def __repr__(self):
        return f"<Agent name={self.name}, role={self.role}, goal={self.goal}>"