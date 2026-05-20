from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def credibility_agent(citations: str) -> str:
    print("[Credibility Agent] Scoring sources...")

    prompt = f"""You are a source credibility expert.
Analyze the following citations and rate each one.

For each source give:
1. Source name or description
2. Credibility rating: HIGH / MEDIUM / LOW
3. One line reason why

Use this exact format for each source:
🟢 HIGH | source name | reason
🟡 MEDIUM | source name | reason  
🔴 LOW | source name | reason

Citations to analyze:
{citations}

At the end give an Overall Trust Score out of 10."""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content