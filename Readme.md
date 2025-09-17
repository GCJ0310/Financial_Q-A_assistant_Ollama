# 💰 Financial Document Q&A Assistant

A **web-based assistant** that processes financial PDF or Excel documents and answers user questions using **natural language**.

This tool is built with **Streamlit** for the interface and **LangChain** + **Ollama** for local Small Language Model (SLM) integration, ensuring your financial data stays private and secure on your machine.

---

## ✨ Features

- **Document Processing:** Upload financial documents in PDF or Excel format (e.g., Income Statement, Balance Sheet, Cash Flow Statement).
- **Data Extraction:** Automatically extracts both text and numerical data from your documents.
- **Natural Language Q&A:** Ask questions about key financial metrics like revenue, expenses, profits, and more using plain English.
- **Conversational Memory:** Supports follow-up questions by remembering the context of your previous queries.
- **Intuitive UI:** An interactive chat interface with a **conversation history in the sidebar** and a clean, user-friendly design.
- **Document Preview:** Easily preview the content extracted from your uploaded documents.

---

## 💻 Technical Details

- **Frontend:** Streamlit
- **Backend:** Python, LangChain, Ollama SLM
- **Document Processing:** Uses `pdfplumber` for PDFs and `pandas` + `openpyxl` for Excel files.
- **Conversation Memory:** A built-in system tracks previous questions and answers to maintain context.
- **Model Used:** The current default model is **LLaMA2**, but for significantly faster responses, **phi:latest** is highly recommended.

---

## 📂 File Structure

```

Financial-QA-Assistant/
│
├─ app.py              \# The main Streamlit interface and chat logic
├─ qa.py        \# Manages the question-answering process with Ollama
├─ doc_processing.py   \# Functions for reading and cleaning PDF and Excel files
├─ utils.py            \# Helper functions (e.g., text chunking)
├─ requirements.txt    \# Lists all necessary Python dependencies
└─ README.md           \# This file

````

---

## ⚙️ Setup Instructions

Follow these steps to get the application running on your local machine.

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd Financial-Q-A-assistant_Ollama
````

### 2\. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

  - **On Windows (PowerShell):**
    ```bash
    .\venv\Scripts\Activate.ps1
    ```
  - **On Windows (CMD):**
    ```bash
    .\venv\Scripts\activate.bat
    ```
  - **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 3\. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 4\. Install dependencies

```bash
pip install -r requirements.txt
```

### 5\. Pull a local Ollama model

You'll need to have Ollama installed and running. For a quick start, pull the recommended `phi:latest` model, which offers faster inference.

```bash
ollama pull phi:latest
```

> **Note:** The current setup uses LLaMA2, which can be slower, especially with larger documents. For better performance, configure `qa.py` to use `phi:latest`.

### 6\. Run the app

```bash
streamlit run app.py
```

-----

## 🚀 Usage

1.  **Upload:** In the main interface, use the file uploader to select a PDF or Excel financial document.
2.  **Ask:** Type your questions about the document's content (e.g., "What was the total revenue?", "Can you list the operating expenses?").
3.  **Explore:** Your conversation history will be displayed in the sidebar. You can also expand the "Document Preview" section to see the extracted text.

-----

## 📝 Dependencies

  - Python ≥3.10
  - `Streamlit`
  - `LangChain` & `langchain-community`
  - `Ollama` Python client
  - `pdfplumber`, `pandas`, `openpyxl`

-----

## 📌 Notes & Future Improvements

  - **Performance:** LLaMA2 can be resource-intensive. For faster local inference, it's highly recommended to use `phi:latest`.
  - **Document Size:** The app uses text chunking to handle large documents, but processing time may increase with very large files.
  - **Local Hosting:** The entire application runs locally on your machine, ensuring your data remains private and is never sent to the cloud.

### 💡 Future Plans:

  - **Template Support:** Add support for more diverse financial document layouts and templates.
  - **Summarization:** Implement a feature to generate concise summaries of large financial reports.
  - **Error Handling:** Improve robustness for unsupported file types or corrupted documents.
