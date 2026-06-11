---
title: Quria
emoji: 🔬
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# 🔬 Quria — Research Intelligence

> An autonomous multi-agent AI research assistant that searches, summarizes, cites, validates, and scores sources in real-time.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-1.2.0-green?style=flat-square)
![Chainlit](https://img.shields.io/badge/Chainlit-2.x-pink?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🚀 What is Quria?

Quria is not a chatbot. It is a **research companion** powered by 6 specialized AI agents that work together autonomously to give you deep, validated, and credible research on any topic — in seconds.

Unlike ChatGPT which answers from memory, Quria **goes out and researches in real-time**, adapts its tone to your level, scores every source for credibility, and lets you export results as a professional PDF.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Real-time Research** | Searches the live web using Tavily Search API |
| 🧠 **Smart Tone Detection** | Adapts response style for students, professionals, or casual users |
| 📝 **AI Summarization** | Generates clean structured summaries using Groq LLaMA3 |
| 📚 **Citation Extraction** | Extracts and formats all sources automatically |
| ✅ **Fact Validation** | Checks accuracy and rates confidence level |
| 🛡️ **Source Credibility Scorer** | Rates every source as 🟢 HIGH / 🟡 MEDIUM / 🔴 LOW |
| 🗺️ **Learning Roadmap Generator** | Creates step-by-step learning paths for any topic |
| 💾 **Chat History** | Saves all research sessions with ChatGPT-style sidebar |
| 📄 **PDF Export** | Downloads research as a branded professional PDF report |
| 🔐 **Authentication** | Secure login to protect your research sessions |

---

## 🏗️ Architecture

User Query
│
▼
┌─────────────────────────────────────────┐
│           LangGraph Supervisor          │
│                                         │
│  ┌─────────┐    ┌──────────────────┐   │
│  │Research │───▶│ Summarization    │   │
│  │ Agent   │    │ Agent            │   │
│  └─────────┘    └──────────────────┘   │
│       │                  │             │
│       ▼                  ▼             │
│  ┌─────────┐    ┌──────────────────┐   │
│  │Citation │    │  Validation      │   │
│  │ Agent   │    │  Agent           │   │
│  └─────────┘    └──────────────────┘   │
│                          │             │
│                          ▼             │
│                 ┌──────────────────┐   │
│                 │  Credibility     │   │
│                 │  Agent           │   │
│                 └──────────────────┘   │
└─────────────────────────────────────────┘
│
▼
Chainlit UI (Chat Interface)

---

## 🛠️ Tech Stack

- **LangGraph** — Multi-agent orchestration
- **Groq LLaMA3** — LLM inference (llama-3.3-70b-versatile)
- **ChromaDB** — Vector database for semantic search
- **Sentence Transformers** — Text embeddings (all-MiniLM-L6-v2)
- **Tavily Search API** — Real-time web search
- **Chainlit** — Chat UI with sidebar history
- **FastAPI** — REST API server
- **ReportLab** — PDF generation
- **SQLite + aiosqlite** — Chat history persistence

---

## 📁 Project Structure
quria/
├── agents/
│   ├── research_agent.py       # Web search + RAG retrieval
│   ├── summarization_agent.py  # Tone-aware summarization
│   ├── citation_agent.py       # Source extraction
│   ├── validation_agent.py     # Fact checking
│   ├── credibility_agent.py    # Source scoring
│   ├── roadmap_agent.py        # Learning path generator
│   └── tone_agent.py           # User tone detection
├── rag/
│   └── embedder.py             # ChromaDB + embeddings
├── graph/
│   └── supervisor.py           # LangGraph pipeline
├── api/
│   └── main.py                 # FastAPI server
├── app.py                      # Chainlit UI
├── chat_history.py             # History management
├── config_db.py                # SQLite data layer
├── export_utils.py             # PDF generation
├── .env                        # API keys (not committed)
├── requirements.txt
└── README.md

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-research.git
cd multi-agent-research
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
CHAINLIT_AUTH_SECRET=your_secret_key

### 5. Run the app
```bash
chainlit run app.py -w
```

### 6. Login
- **Email:** `admin@quria.ai`
- **Password:** `quria123`

---

## 🎯 Usage

| What you type | What Quria does |
|---|---|
| `what is quantum computing` | Full research with all 5 agents |
| `roadmap for learning Python` | Generates 8-week learning path |
| `export` | Downloads last research as PDF |
| `history` | Shows past research sessions |
| `clear history` | Resets local history |

---

## 🔑 API Keys

| Service | Purpose | Get it here |
|---|---|---|
| Groq | LLM inference | [console.groq.com](https://console.groq.com) |
| Tavily | Web search | [app.tavily.com](https://app.tavily.com) |

---

## 📄 License

MIT License — feel free to use, modify and distribute.

---

## 👩‍💻 Built by

**Zeba Khan** — AI/ML Developer .

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/zeba-khan-318057285)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/zeba-khan)"." 
