# Pegasus — AI-Powered Market Research Engine

Pegasus is a **production-grade AI market research engine** that autonomously plans research, gathers web intelligence, and synthesizes structured strategic reports using Large Language Models (LLMs).

It is designed to work in **real-world conditions** with unreliable networks, partial data, and long-running research tasks.

Pegasus supports both:
- 🖥️ **GUI Mode** (PyQt5 desktop application)
- ⚙️ **CLI Mode** (headless execution for automation)

---

## ✨ Key Features

- 🧠 **LLM-driven multi-vector research planning**
- 🌐 **Automated web search & content extraction**
- 🔁 **Fault-tolerant crawling** (timeouts, retries, graceful skips)
- 📚 **Per-vector source attribution (citations)**
- 📄 **Export reports as Markdown or PDF**
- 🖥️ **Desktop GUI** and ⚙️ **CLI** from a single codebase
- 🧩 **Modular, extensible architecture**

---

## 🧠 High-Level Architecture

```mermaid
flowchart TD
    A[User Input] --> B[main.py<br/>Mode Dispatcher]

    B --> C[GUI Mode<br/>ui.py]
    B --> D[CLI Mode<br/>cli.py]

    C --> E[RecursiveSectionalAgent<br/>agent.py]
    D --> E

    E --> F[Web Search<br/>DuckDuckGo]
    E --> G[LLM Engine<br/>Ollama]

    F --> H[Vector Summaries<br/>with Sources]
    G --> H

    H --> I[Final Strategic Report<br/>Markdown / PDF]
