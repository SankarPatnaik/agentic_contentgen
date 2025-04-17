from agent_base import Agent

class FinalAgent(Agent):
    def run(self, input_data):
        return f"Final Output:
{input_data['rewritten']}"
