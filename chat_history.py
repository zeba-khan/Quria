import json
import os
from datetime import datetime

HISTORY_FILE = "chat_history.json"

def load_history() -> list:
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_to_history(query: str, summary: str, credibility: str):
    history = load_history()
    entry = {
        "id": len(history) + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "query": query,
        "summary": summary[:300] + "..." if len(summary) > 300 else summary,
        "credibility": credibility[:200] + "..." if len(credibility) > 200 else credibility
    }
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def get_history_text() -> str:
    history = load_history()
    if not history:
        return "📭 No research history yet."
    
    text = "## 📂 Your Research History\n\n"
    for entry in reversed(history[-10:]):  # show last 10
        text += f"**#{entry['id']} — {entry['timestamp']}**\n"
        text += f"🔍 **Query:** {entry['query']}\n"
        text += f"📝 **Summary:** {entry['summary']}\n"
        text += f"🛡️ **Credibility:** {entry['credibility']}\n"
        text += "---\n"
    return text

def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    return "✅ History cleared."