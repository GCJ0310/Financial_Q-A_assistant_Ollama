import streamlit as st
from doc_processing import read_pdf, read_excel, clean_text
from qa import answer_question

st.set_page_config(page_title="Financial Q&A Assistant", layout="wide", page_icon="💰")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'feedback' not in st.session_state:
    st.session_state.feedback = {}

st.markdown("<h1 style='text-align: center; color: darkblue;'>💰 Financial Document Q&A Assistant</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Conversation")
    if st.session_state.chat_history:
        for i, entry in enumerate(st.session_state.chat_history):
            if entry["role"] == "user":
                preview = entry["content"][:25] + ("..." if len(entry["content"]) > 25 else "")
                st.markdown(f"**Q{i//2 + 1}:** {preview}")
    else:
        st.info("No questions yet. Ask something after uploading a document.")

with st.expander("How to Use"):
    st.write("""
    1. Upload a financial PDF or Excel document.  
    2. Ask questions about revenue, expenses, profits, or other financial metrics.  
    3. Your conversation history is saved in the sidebar.  
    4. Rate responses with 👍 or 👎 to give feedback. 👎 will trigger an improved answer.  
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
                st.session_state.chat_history.append({"role": "user", "content": question})
                st.session_state.chat_history.append({"role": "assistant", "content": answer})

            # Show answer box
            st.markdown(f"""
            <div style='background-color:#E0F7FA; padding:15px; border-radius:10px; margin-bottom:10px;'>
                <strong>Answer:</strong> {answer}
            </div>
            """, unsafe_allow_html=True)

            # Feedback buttons
            feedback_col1, feedback_col2 = st.columns([0.1, 0.9])
            with feedback_col1:
                if st.button("👍", key=f"up_{len(st.session_state.chat_history)}"):
                    st.session_state.feedback[len(st.session_state.chat_history)] = "up"
                    st.success("Thanks for your feedback!")

            with feedback_col2:
                if st.button("👎", key=f"down_{len(st.session_state.chat_history)}"):
                    st.session_state.feedback[len(st.session_state.chat_history)] = "down"
                    st.warning("Reworking answer for better clarity...")

                    # Re-run model with improvement flag
                    improved_answer = answer_question(document_text, question + " (Please explain in more detail and simpler language)")
                    
                    # Replace last assistant answer with improved one
                    st.session_state.chat_history[-1]["content"] = improved_answer

                    # Show improved answer immediately
                    st.markdown(f"""
                    <div style='background-color:#FFF3E0; padding:15px; border-radius:10px; margin-bottom:10px;'>
                        <strong>Improved Answer:</strong> {improved_answer}
                    </div>
                    """, unsafe_allow_html=True)

    with col2:
        st.subheader("Document Preview")
        with st.expander("Show Document Text"):
            st.write(document_text[:1500] + " ...")
