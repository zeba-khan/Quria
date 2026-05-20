from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

# llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-8b-8192")
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def validation_agent(summary: str) -> str:
    print("[Validation Agent] Validating summary...")

    prompt = f"""You are a fact validator.
Review the following research summary and:
1. Check for any inconsistencies or vague claims
2. Rate the confidence level (High / Medium / Low)
3. Suggest any improvements

Summary:
{summary}"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content