from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

# llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-8b-8192")
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def citation_agent(context: str) -> str:
    print("[Citation Agent] Extracting citations...")

    prompt = f"""You are a citation extractor.
From the following research context, extract and list all key facts, 
sources, and references in a numbered list:

{context}

Format each citation clearly."""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content