class AgentFSM:
    def __init__(self):
        self.state = "PLAN"
        self.history = []

    def step(self, env: dict):
        if self.state == "PLAN":
            self.history.append("plan")
            self.state = "ACT"
        elif self.state == "ACT":
            self.history.append("act")
            self.state = "OBSERVE"
        elif self.state == "OBSERVE":
            self.history.append("observe")
            self.state = "REFLECT"
        elif self.state == "REFLECT":
            self.history.append("reflect")
            self.state = "DONE" if env.get("task_complete") else "PLAN"

    def run(self, env: dict, max_steps: int = 20) -> list[str]:
        steps = 0
        while self.state != "DONE" and steps < max_steps:
            self.step(env)
            steps += 1
        return self.history