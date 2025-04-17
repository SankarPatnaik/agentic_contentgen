from agent_base import Agent

class RewriterAgent(Agent):
    def run(self, input_data):
        text = input_data["generated"]
        return {"rewritten": f"Improved version: {text}"}
