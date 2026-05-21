from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
from agents.tone_agent import detect_tone, get_tone_instruction

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def summarization_agent(context: str, query: str = "") -> str:
    print("[Summarization Agent] Detecting tone and summarizing...")

    tone = detect_tone(query)
    tone_instruction = get_tone_instruction(tone)

    print(f"[Summarization Agent] Detected tone: {tone}")

    prompt = f"""You are a research summarizer.
{tone_instruction}

Summarize the following research context:

{context}

Provide a well-structured summary."""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content