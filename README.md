# ContentGen Agentic AI

This project demonstrates an agentic AI framework to process user inputs (questions/statements) and generate high-quality, rephrased content using modular agents.

## Agents
- **InputHandlerAgent**: Classifies input type.
- **ResearchAgent**: Simulates research (can be extended with web scraping or APIs).
- **ContentGeneratorAgent**: Generates content.
- **RewriterAgent**: Enhances quality.
- **FinalAgent**: Produces the final output.

## Run
```bash
python main.py
```

## Future Improvements
- Integrate LangGraph or CrewAI
- Add real research via web or vector DB
- Tone/style customization
