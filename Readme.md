# 💰 Financial Document Q&A Assistant

A **local web-based assistant** to process your financial PDF or Excel documents and answer your questions in **plain English**.

This project runs entirely on your machine using **Streamlit** for the interface and **Ollama** for local Small Language Model (SLM) inference.  
➡️ Your financial data stays **private** — it never leaves your computer.

---

## ✨ Features

- **Document Upload:** Add financial PDFs or Excel files (Balance Sheet, Income Statement, Cash Flow Report, etc.).
- **Smart Q&A:** Ask questions like *“What was the revenue last year?”* and get clear, step-by-step answers.
- **Friendly Conversation:** The assistant greets you, explains concepts in **beginner-friendly language**, and avoids jargon.
- **Adaptive Tone:**  
  - 📊 **Numbers & Metrics:** Formal, structured answers.  
  - 💬 **Explanations:** Simple, friendly style.
- **Conversation History:** Sidebar remembers your previous questions.
- **Document Preview:** See the extracted text from your uploaded file.

---

## 🧠 Prompt Improvements

The system prompt is designed so responses:  
- ✅ Greet the user before answering  
- ✅ Use **simple, beginner-friendly language**  
- ✅ Break complex answers into **clear bullet points or steps**  
- ✅ End with a **short summary / key takeaway**  
- ✅ Adjust tone automatically (formal for financial numbers, casual for explanations)

**Example:**  
- *User asks:* “What is the net profit margin?”  
  - Assistant gives a **formal calculation breakdown**  
- *User asks:* “What does gross margin mean?”  
  - Assistant explains in **everyday language** with an example

---

## 💻 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python + LangChain + Ollama  
- **Document Reading:** `pdfplumber` (PDFs), `pandas` + `openpyxl` (Excel)  
- **Model:** Default is **llama2**; `phi:latest` is recommended for faster answers

---

## 📂 File Structure

```
Financial_Q-A_Assistant_Ollama/
│
├── app.py             # Main Streamlit interface
├── qa.py       # Q&A logic with Ollama + prompt improvements
├── doc_processing.py  # Reads and cleans PDF/Excel
├── utils.py           # Helper functions (e.g., text chunking)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

## ⚙️ Setup (Local Only)

1. **Clone the project**  
   ```bash
   git clone <your-repo-link>
   cd Financial_Q-A_Assistant_Ollama
   ```

2. **Create and activate virtual environment**

   - Windows PowerShell:
     ```bash
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Windows CMD:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate.bat
     ```
   - Mac/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. **Upgrade pip**
   ```bash
   python -m pip install --upgrade pip
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Ollama**  
   Download and install Ollama from [ollama.ai/download](https://ollama.ai/download)

6. **Pull a model**  
   By default, the app uses llama2:
   ```bash
   ollama pull llama2
   ```
   ⚡ For faster inference, you can also pull phi:latest:
   ```bash
   ollama pull phi:latest
   ```
   > You can switch the model in `qa.py`.

7. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🚀 How to Use

- Upload a file → PDF or Excel
- Ask questions → e.g., “What is total revenue?”, “Explain gross margin”
- View history → Conversation appears in the sidebar
- Check document preview → Expand to see extracted content

---

## 📝 Dependencies

- Python ≥ 3.10
- streamlit
- langchain, langchain-community
- ollama client
- pdfplumber, pandas, openpyxl

---

## 📌 Notes & Future Plans

- ⚡ **Performance:** LLaMA2 works well but can be slower. For faster local inference, use phi:latest.
- 📄 **Large files:** The app splits text into chunks for smooth processing.
- 🔒 **Privacy:** Runs 100% locally — your data never leaves your machine.

**Planned improvements:**
- Auto-summary of large reports
- Support for more financial document templates
- Stronger error handling for bad file formats

---

**Feel free to open issues or contribute!**
