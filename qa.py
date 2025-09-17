# import ollama
# from utils import chunk_text
# from datetime import datetime

# conversation_history = []

# def answer_question(document_text, question):
#     conversation_history.append({'role':'user','content':question,'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

#     chunks = chunk_text(document_text, max_words=500)
#     document_content = ""
#     for i, chunk in enumerate(chunks):
#         document_content += f"Document Chunk {i+1}:\n{chunk}\n"

#     full_prompt = "You are a financial assistant. Answer based only on the provided document.\n\n"
#     for msg in conversation_history[:-1]:
#         role = "User" if msg['role']=='user' else "Assistant"
#         full_prompt += f"{role}: {msg['content']}\n"

#     full_prompt += f"Document:\n{document_content}\nQuestion: {question}\nAnswer concisely."

#     try:
#         response = ollama.chat(model="phi:latest", messages=[{"role":"user","content":full_prompt}])
#         answer = response.content
#     except Exception as e:
#         answer = f"Error with SLM model: {e}"

#     conversation_history.append({'role':'assistant','content':answer,'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
#     return answer

from langchain_community.llms import Ollama
from utils import chunk_text
from datetime import datetime

# Initialize LangChain Ollama LLM
llm = Ollama(model="llama2", base_url="http://localhost:11434", verbose=True)

conversation_history = []

def answer_question(document_text, question):
    conversation_history.append({'role': 'user', 'content': question, 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

    # Chunk document to avoid overloading the model
    chunks = chunk_text(document_text, max_words=500)
    document_content = ""
    for i, chunk in enumerate(chunks):
        document_content += f"Document Chunk {i+1}:\n{chunk}\n"

    # Build prompt including conversation history
    prompt = "You are a financial assistant. Answer questions based ONLY on the provided document.\n\n"
    for msg in conversation_history[:-1]:
        role = "User" if msg['role'] == 'user' else "Assistant"
        prompt += f"{role}: {msg['content']}\n"

    prompt += f"Document:\n{document_content}\nQuestion: {question}\nAnswer concisely."

    try:
        response = llm.invoke(prompt)
        answer = response
    except Exception as e:
        answer = f"Error with SLM model: {e}"

    conversation_history.append({'role': 'assistant', 'content': answer, 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    return answer
