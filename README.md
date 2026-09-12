# ResearchBench-GenAI-Workspace-project
An AI-powered, evidence-grounded persistent workspace for biotechnology &amp; life sciences research with automated safety compliance and protocol tracking.






# 🧬 ResearchBench AI
> **HEC / Aspire GenAI Hackathon MVP**  
> *Designed & Developed by: **Arsalan & Habiba***

---

### 📌 Project Overview
**ResearchBench AI** is a lightweight, AI-powered persistent research workspace built specifically for biotechnology and life-science students and researchers.

Standard LLMs often lose context or hallucinate when processing complex scientific literature. ResearchBench AI bridges this gap by combining **Grounded RAG (Retrieval-Augmented Generation)** with a **Persistent SQLite Memory**, ensuring that a researcher's reading, personal thoughts, laboratory protocols, and experimental observations remain explicitly connected.

---

### 🌟 Key Core Features & Modules

* **📚 1. Research Library & PDF Reader**
  * Upload biotechnology research papers and laboratory protocols.
  * Extract document text and view original contents directly inside the app workspace.

* **🤖 2. Evidence-Grounded AI Assistant**
  * Perform evidence-backed Q&A queries on uploaded scientific papers.
  * Displays precise **Source Citations & Evidence Snippets** to eliminate scientific hallucination.

* **🧠 3. Persistent Research Memory**
  * Save personal notes, hypotheses, research questions, and experimental observations.
  * Stores student reasoning in a local SQLite database separate from AI conclusions.

* **📋 4. Protocol Companion & Safety Engine**
  * Extract protocol steps into interactive, step-by-step lab checklists.
  * Automatically scans reagents against a safety dictionary to display PPE and safety warnings.

* **🗺️ 5. Research Journey & Dashboard**
  * View chronological event history tracking progress from literature discovery to experimental execution.
  * Real-time metrics dashboard to inspect workspace database status.

---

### 🛠️ Tech Stack & Architecture
* **Frontend UI:** Streamlit (Multi-Page Architecture)
* **Backend Runtime:** Python 3.10+
* **PDF Extraction:** PyPDF
* **Database & Storage:** SQLite3 (Persistent Memory Engine)
