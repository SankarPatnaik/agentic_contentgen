from input_handler import InputHandlerAgent
from research_agent import ResearchAgent
from content_generator import ContentGeneratorAgent
from rewriter_agent import RewriterAgent
from final_agent import FinalAgent

def main(user_input):
    input_handler = InputHandlerAgent("InputHandler")
    research_agent = ResearchAgent("ResearchAgent")
    generator_agent = ContentGeneratorAgent("ContentGenerator")
    rewriter_agent = RewriterAgent("RewriterAgent")
    final_agent = FinalAgent("FinalAgent")

    step1 = input_handler.run(user_input)
    step2 = research_agent.run(step1)
    step3 = generator_agent.run(step2)
    step4 = rewriter_agent.run(step3)
    result = final_agent.run(step4)
    
    print(result)

if __name__ == "__main__":
    user_input = input("Enter your question or statement: ")
    main(user_input)
