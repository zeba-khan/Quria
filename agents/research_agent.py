"""This agent:

Searches the web using Tavily
Stores results into ChromaDB
Retrieves the most relevant chunks back """


from tavily import TavilyClient
from rag.embedder import search_documents, add_documents
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def research_agent(query: str) -> str:
    print(f"[Research Agent] Searching for: {query}")

    # Step 1: Search the web with Tavily
    response = tavily.search(query=query, max_results=5)
    web_results = [r["content"] for r in response["results"]]

    # Step 2: Store results in ChromaDB
    ids = [f"doc_{i}" for i in range(len(web_results))]
    add_documents(web_results, ids)

    # Step 3: Retrieve most relevant chunks
    relevant_docs = search_documents(query, n_results=3)

    # Step 4: Combine into context
    context = "\n\n".join(relevant_docs)
    print(f"[Research Agent] Found {len(relevant_docs)} relevant chunks")

    return context