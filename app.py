import streamlit as st
from doc_processing import read_pdf, read_excel, clean_text
from qa import answer_question

st.set_page_config(page_title="Financial Q&A Assistant", layout="wide", page_icon="💰")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.markdown("<h1 style='text-align: center; color: darkblue;'>💰 Financial Document Q&A Assistant</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Conversation History")
    if st.session_state.chat_history:
        for entry in st.session_state.chat_history:
            role, text = entry.split(":", 1)
            if role.strip() == "User":
                st.markdown(f"**You:** {text.strip()}")
            else:
                st.markdown(f"**Assistant:** {text.strip()}")
    else:
        st.info("No questions asked yet.")

with st.expander("How to Use"):
    st.write("""
    1. Upload a financial PDF or Excel document.  
    2. Ask questions about revenue, expenses, profits, or other financial metrics.  
    3. Conversation history is shown in the sidebar.  
    """)

uploaded_file = st.file_uploader("Upload PDF or Excel financial document", type=["pdf", "xlsx"])

if uploaded_file:
    st.success("File uploaded successfully!")

    if uploaded_file.type == "application/pdf":
        document_text = read_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        document_text = read_excel(uploaded_file)
    else:
        st.error("Unsupported file type")
        st.stop()

    document_text = clean_text(document_text)

    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("Ask a Question")
        question = st.text_input("Enter your question:")

        if question:
            with st.spinner("Processing..."):
                answer = answer_question(document_text, question)
                st.session_state.chat_history.append(f"User: {question}")
                st.session_state.chat_history.append(f"Assistant: {answer}")

            st.markdown(f"""
            <div style='background-color:#E0F7FA; padding:15px; border-radius:10px; margin-bottom:10px;'>
                <strong>Answer:</strong> {answer}
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.subheader("Document Preview")
        with st.expander("Show Document Text"):
            st.write(document_text[:1500] + " ...")
