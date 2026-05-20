from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from graph.supervisor import run_pipeline
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(
    title="Multi-Agent Research Assistant",
    description="AI-powered research using LangGraph, ChromaDB, and Groq LLaMA3",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory=".chainlit/public"), name="static")


# Request model
class ResearchRequest(BaseModel):
    query: str

# Response model
class ResearchResponse(BaseModel):
    query: str
    summary: str
    citations: str
    validation: str

@app.get("/health")
def health_check():
    return {"status": "running"}

@app.post("/research", response_model=ResearchResponse)
def run_research(request: ResearchRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    print(f"[API] Received query: {request.query}")
    result = run_pipeline(request.query)

    return ResearchResponse(
        query=result["query"],
        summary=result["summary"],
        citations=result["citations"],
        validation=result["validation"]
    )
    
    
if __name__ == "__main__":
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=True)    