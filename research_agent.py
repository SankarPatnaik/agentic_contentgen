from agent_base import Agent

class ResearchAgent(Agent):
    def run(self, input_data):
        # Simulated research output
        return {"research": f"Simulated research for: {input_data['content']}"}
