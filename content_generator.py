from agent_base import Agent

class ContentGeneratorAgent(Agent):
    def run(self, input_data):
        content = input_data.get("research", "") or input_data["content"]
        return {"generated": f"Generated content based on: {content}"}
