from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.research_agent import research_agent
from agents.summarization_agent import summarization_agent
from agents.citation_agent import citation_agent
from agents.validation_agent import validation_agent
from agents.credibility_agent import credibility_agent

class ResearchState(TypedDict):
    query: str
    context: str
    summary: str
    citations: str
    validation: str
    credibility: str

def run_research(state: ResearchState) -> ResearchState:
    context = research_agent(state["query"])
    return {**state, "context": context}

def run_summarization(state: ResearchState) -> ResearchState:
    summary = summarization_agent(state["context"], state["query"])
    return {**state, "summary": summary}

def run_citation(state: ResearchState) -> ResearchState:
    citations = citation_agent(state["context"])
    return {**state, "citations": citations}

def run_validation(state: ResearchState) -> ResearchState:
    validation = validation_agent(state["summary"])
    return {**state, "validation": validation}

def run_credibility(state: ResearchState) -> ResearchState:
    credibility = credibility_agent(state["citations"])
    return {**state, "credibility": credibility}

def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("research", run_research)
    graph.add_node("summarize", run_summarization)
    graph.add_node("cite", run_citation)
    graph.add_node("validate", run_validation)
    graph.add_node("credibility", run_credibility)

    graph.set_entry_point("research")
    graph.add_edge("research", "summarize")
    graph.add_edge("summarize", "cite")
    graph.add_edge("cite", "validate")
    graph.add_edge("validate", "credibility")
    graph.add_edge("credibility", END)

    return graph.compile()

def run_pipeline(query: str) -> ResearchState:
    app = build_graph()
    initial_state = ResearchState(
        query=query,
        context="",
        summary="",
        citations="",
        validation="",
        credibility=""
    )
    result = app.invoke(initial_state)
    return result