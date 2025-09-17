# 💰 Financial Document Q&A Assistant

A **web-based assistant** that processes financial PDF or Excel documents and answers user questions using **natural language**.  
Built with **Streamlit** for the interface and **LangChain + Ollama** for local Small Language Model (SLM) integration.  

---

## Features

- Upload PDF or Excel financial documents (Income Statement, Balance Sheet, Cash Flow, etc.)
- Extract text and numerical data automatically
- Ask questions about revenue, expenses, profits, and other financial metrics
- Supports follow-up questions using conversation memory
- Interactive chat interface with **conversation history in the sidebar**
- Preview uploaded document content
- Clean and intuitive UI with color-coded answer boxes

---

## Technical Details

- **Frontend:** Streamlit  
- **Backend:** Python, LangChain, Ollama SLM  
- **Document Processing:** `pdfplumber` for PDFs, `pandas` + `openpyxl` for Excel  
- **Conversation Memory:** Tracks previous questions and answers for context  
- **Model Used:** Currently **LLaMA2**, but for faster responses, **phi:latest** is recommended  

---

## File Structure

- Financial-QA-Assistant/
│
├─ app.py # Streamlit interface with chat sidebar
├─ qa_system.py # Handles question-answering using Ollama
├─ doc_processing.py # Functions to read and clean PDF/Excel
├─ utils.py # Helper functions like chunk_text
├─ requirements.txt # Python dependencies
└─ README.md

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd Financial-QA-Assistant
2. Create a virtual environment
bash
Copy code
python -m venv venv
# Activate on Windows
venv\Scripts\Activate.ps1  # PowerShell
venv\Scripts\activate.bat  # CMD
3. Upgrade pip
bash
Copy code
python -m pip install --upgrade pip
4. Install dependencies
bash
Copy code
pip install -r requirements.txt
5. Pull a local Ollama model
Recommended for faster responses: phi:latest

bash
Copy code
ollama pull phi:latest
Current setup uses LLaMA2, which may be slower for large documents.

6. Run the app
bash
Copy code
streamlit run app.py
Usage
Upload a PDF or Excel financial document in the main interface.

Ask questions about revenue, expenses, profits, or other financial metrics.

Conversation history is displayed in the sidebar.

Expand "Document Preview" to see the extracted text.

Dependencies
Python ≥3.10

Streamlit

LangChain & langchain-community

Ollama Python client

pdfplumber, pandas, openpyxl

Notes
Performance: LLaMA2 can be heavy; use phi:latest for faster local inference.

Document Size: Large documents may take longer; chunking is used to improve speed.

Local Hosting: Everything runs locally; no cloud deployment is needed.

Future Improvements
Support more financial document layouts and templates

Add summarization for very large reports


Improve error handling for unsupported file types or corrupted documents
