from agent_base import Agent

class InputHandlerAgent(Agent):
    def run(self, input_data):
        if "?" in input_data.strip():
            return {"type": "question", "content": input_data}
        return {"type": "statement", "content": input_data}
