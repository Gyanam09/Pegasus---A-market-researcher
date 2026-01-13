# Pegasus — AI-Powered Market Research Engine

Pegasus is a **production-grade AI market research system** that autonomously generates research vectors, mines web intelligence, synthesizes structured strategic insights, and exports professional reports in **Markdown or PDF** format.

The system supports both:
- 🖥️ **Graphical User Interface (GUI)** using PyQt5  
- ⚙️ **Command-Line Interface (CLI)** for headless and automated execution  

---

## 🚀 Key Features

- 🧠 **LLM-driven research planning** (multi-vector analysis)
- 🌐 **Automated web search & content extraction**
- 🔁 **Retry-safe & fallback-enabled AI calls**
- 📚 **Per-vector source attribution (citations)**
- 📄 **Professional PDF & Markdown export**
- 🖥️ **Desktop GUI (PyQt5)**
- ⚙️ **CLI mode for automation**
- 🧩 **Single unified launcher (`main.py`)**

---

## 🧠 High-Level Architecture

            ┌──────────────┐
            │   User Input │
            └──────┬───────┘
                   │
      ┌────────────▼────────────┐
      │        main.py           │
      │   (Mode Dispatcher)      │
      └──────┬──────────┬───────┘
             │          │
    ┌────────▼───┐   ┌──▼────────┐
    │   GUI Mode  │   │ CLI Mode  │
    │  (ui.py)   │   │ (cli.py)  │
    └──────┬─────┘   └────┬──────┘
           │              │
           └──────┬───────┘
                  ▼
    ┌──────────────────────────┐
    │ RecursiveSectionalAgent  │
    │        (agent.py)        │
    └──────┬─────────┬────────┘
           │         │
 ┌─────────▼───┐ ┌───▼─────────┐
 │ Web Search  │ │  LLM Engine │
 │  (DDGS)     │ │  (Ollama)   │
 └─────────┬───┘ └────┬────────┘
           │          │
    ┌──────▼──────────▼──────┐
    │ Vector Summaries with   │
    │ Source Attribution      │
    └──────────┬──────────────┘
               ▼
    ┌─────────────────────────┐
    │ Final Strategic Report  │
    │  (Markdown / PDF)       │
    └─────────────────────────┘


---

## 🔍 How Pegasus Works

1. **Research Vector Generation**  
   The LLM generates multiple focused research queries for a given topic.

2. **Web Intelligence Mining**  
   Each vector triggers:
   - DuckDuckGo search
   - Safe URL fetching with timeouts
   - Content extraction via Trafilatura

3. **Vector-Level Summarization**  
   Each research vector is summarized independently along with its sources.

4. **Master Report Synthesis**  
   All vector summaries are combined into a structured strategic report.

5. **Export**  
   Reports can be exported as:
   - `.md` (Markdown)
   - `.pdf` (Professional PDF using ReportLab)

---

## 🖥️ Usage

### ▶️ GUI Mode (Default)
```bash
python main.py

▶️ GUI Mode (Explicit)
python main.py gui
▶️ CLI Mode
python main.py cli "AI semiconductor market overview"

▶️ CLI Mode + PDF Export
python main.py cli "AI semiconductor market overview" --pdf

🔐 Environment Setup

Pegasus requires an Ollama API key.

Windows (PowerShell)
setx OLLAMA_API_KEY "your_api_key_here"

Linux / macOS
export OLLAMA_API_KEY="your_api_key_here"


Restart the terminal after setting the variable.

🧰 Tech Stack

Python 3.10+

Ollama (LLM inference)

PyQt5 (GUI)

DuckDuckGo Search (ddgs)

Trafilatura (web extraction)

ReportLab (PDF generation)

📌 Use Cases

Market & competitor analysis

Strategic planning and forecasting

Due diligence research

Consulting & analytics workflows

AI-assisted knowledge synthesis