from langchain_community.llms import Ollama
from utils import chunk_text
from datetime import datetime

# Initialize LangChain Ollama LLM
llm = Ollama(model="llama2", base_url="http://localhost:11434", verbose=True)

conversation_history = []

def answer_question(document_text, question):
    conversation_history.append({
        'role': 'user', 
        'content': question, 
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

    # Chunk document
    chunks = chunk_text(document_text, max_words=500)
    document_content = ""
    for i, chunk in enumerate(chunks):
        document_content += f"Document Chunk {i+1}:\n{chunk}\n"

    # Enhanced adaptive prompt
    prompt = """You are a helpful **Financial Assistant**.
When answering:
1. Always greet the user first.
2. Adapt your tone:
   - If the question is about numbers, revenue, profit, growth, ratios, or percentages → use a **formal, professional style** with structured points.
   - If the question is about explanations, meaning, or general insights → use a **friendly, simple style** with easy language.
3. Break down complex answers into **clear steps or bullet points**.
4. End with a **short summary or key takeaway**.
5. Base your answer ONLY on the provided document text. If info is missing, politely say so.
6. Never use heavy jargon without explaining it.

Here is the conversation so far:
"""

    # Add conversation history
    for msg in conversation_history[:-1]:
        role = "User" if msg['role'] == 'user' else "Assistant"
        prompt += f"{role}: {msg['content']}\n"

    # Add current document and question
    prompt += f"""
Document:
{document_content}

User Question: {question}

Now, reply by following the above rules.
"""

    try:
        response = llm.invoke(prompt)
        answer = response
    except Exception as e:
        answer = f"Error with SLM model: {e}"

    conversation_history.append({
        'role': 'assistant',
        'content': answer,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    return answer
