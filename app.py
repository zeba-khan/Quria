import os
import chainlit as cl
from agents.roadmap_agent import roadmap_agent
from graph.supervisor import run_pipeline
from chat_history import save_to_history, get_history_text, clear_history
from export_utils import export_to_pdf
from dotenv import load_dotenv

load_dotenv()

@cl.on_chat_start
async def start():
    await cl.Message(
        content="""Hey! 👋 I'm **Quria**, your AI research companion.

I research, summarize, cite, and fact-check any topic in real-time.

*What would you like to explore today?* 🚀"""
    ).send()

@cl.on_message
async def main(message: cl.Message):
    query = message.content.strip()

    if query.lower() == "history":
        history_text = get_history_text()
        await cl.Message(content=history_text).send()
        return

    if query.lower() == "clear history":
        result = clear_history()
        await cl.Message(content=result).send()
        return

    if query.lower() == "export":
        last_result = cl.user_session.get("last_result")
        if not last_result:
            await cl.Message(content="⚠️ No research to export yet. Ask me something first!").send()
            return
        await cl.Message(content="📄 Generating your PDF report...").send()
        filepath = export_to_pdf(
            query=last_result["query"],
            summary=last_result["summary"],
            citations=last_result["citations"],
            credibility=last_result["credibility"],
            validation=last_result["validation"]
        )
        elements = [cl.File(name="Quria Research Report.pdf", path=filepath, display="inline")]
        await cl.Message(content="✅ Your PDF is ready!", elements=elements).send()
        return

    if any(word in query.lower() for word in ["roadmap", "learn", "how to learn", "learning path", "guide me", "where to start"]):
        thinking_msg = cl.Message(content="🗺️ Generating your personalized learning roadmap...")
        await thinking_msg.send()
        roadmap = roadmap_agent(query)
        await thinking_msg.remove()
        await cl.Message(content=roadmap).send()
        return

    async with cl.Step(name="🔍 Research Agent") as step:
        step.input = query
        await cl.sleep(1)
        step.output = "Searching web & retrieving documents..."

    async with cl.Step(name="📝 Summarization Agent") as step:
        step.input = "Analyzing tone & summarizing..."
        await cl.sleep(1)
        step.output = "Generating structured summary..."

    async with cl.Step(name="📚 Citation Agent") as step:
        step.input = "Extracting citations..."
        await cl.sleep(1)
        step.output = "Formatting sources..."

    async with cl.Step(name="✅ Validation Agent") as step:
        step.input = "Validating facts..."
        await cl.sleep(1)
        step.output = "Checking accuracy..."

    async with cl.Step(name="🛡️ Credibility Agent") as step:
        step.input = "Scoring sources..."
        await cl.sleep(1)
        step.output = "Analyzing source reliability..."

    thinking_msg = cl.Message(content="⏳ Quria is researching this for you...")
    await thinking_msg.send()

    try:
        result = run_pipeline(query)
        save_to_history(query, result['summary'], result['credibility'])

        cl.user_session.set("last_result", {
            "query": query,
            "summary": result['summary'],
            "citations": result['citations'],
            "credibility": result['credibility'],
            "validation": result['validation']
        })

        response = f"""## 📋 Research Results for: *{query}*

---

### 📝 Summary
{result['summary']}

---

### 📚 Citations
{result['citations']}

---

### 🛡️ Source Credibility
{result['credibility']}

---

### ✅ Validation
{result['validation']}

---
💾 *Saved to history · Type `history` to view · Type `export` to download as PDF*"""

        await thinking_msg.remove()
        await cl.Message(content=response).send()

    except Exception as e:
        await thinking_msg.remove()
        await cl.Message(content=f"❌ Quria ran into an error: {str(e)}").send()