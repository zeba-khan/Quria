from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def detect_tone(query: str) -> str:
    prompt = f"""Analyze this user query and classify the user type.
Query: "{query}"

Reply with ONLY one word from these options:
- student (if the query sounds like learning, homework, thesis, basics)
- professional (if the query sounds like business, market, analysis, strategy)
- casual (if the query sounds like general curiosity, news, simple questions)

Reply with just one word, nothing else."""

    response = llm.invoke([HumanMessage(content=prompt)])
    tone = response.content.strip().lower()

    if tone not in ["student", "professional", "casual"]:
        tone = "casual"

    return tone


def get_tone_instruction(tone: str) -> str:
    instructions = {
        "student": "Explain in simple, easy-to-understand language. Use examples and analogies. Avoid complex jargon. Make it feel like a teacher explaining to a student.",
        "professional": "Provide a formal, data-driven, analytical response. Use professional language. Focus on insights, trends, and actionable information.",
        "casual": "Be friendly, conversational and concise. Get to the point quickly. Use simple language like explaining to a friend."
    }
    return instructions.get(tone, instructions["casual"])