from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def roadmap_agent(query: str) -> str:
    print("[Roadmap Agent] Generating learning roadmap...")

    prompt = f"""You are an expert learning path designer.
The user wants to learn about: "{query}"

Create a detailed step-by-step learning roadmap with this exact format:

🗺️ LEARNING ROADMAP: {query}

📍 PHASE 1 — FOUNDATIONS (Week 1-2)
- Step 1: [topic] — [why it's important]
- Step 2: [topic] — [why it's important]
- Step 3: [topic] — [why it's important]

📍 PHASE 2 — CORE CONCEPTS (Week 3-4)
- Step 1: [topic] — [why it's important]
- Step 2: [topic] — [why it's important]
- Step 3: [topic] — [why it's important]

📍 PHASE 3 — ADVANCED TOPICS (Week 5-6)
- Step 1: [topic] — [why it's important]
- Step 2: [topic] — [why it's important]
- Step 3: [topic] — [why it's important]

📍 PHASE 4 — PRACTICAL APPLICATION (Week 7-8)
- Step 1: [project/practice] — [what you'll build/do]
- Step 2: [project/practice] — [what you'll build/do]

🎯 END GOAL: [What the user will be able to do after completing this roadmap]

📚 RECOMMENDED RESOURCES:
- [Resource 1]
- [Resource 2]
- [Resource 3]"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content