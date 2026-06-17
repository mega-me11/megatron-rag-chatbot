import streamlit as st
from utils.pdf_loader import load_pdf   #reads PDF and extracts text
from utils.chunker import chunk_text    #splits text into small pieces
from utils.vector_store import store_chunks, search, reset_db   #stores embeddings in ChromaDB, retrieves relevant chunks, clears old pdf data
from utils.llm import generate_answer    #sends prompt to LLM (Llama3)

st.set_page_config(page_title="Megatron RAG", layout="wide")   #page setup

st.title("🤖 Megatron RAG Chatbot 🤖")

# -----------------------                   
# MODE SELECTION                                 #RAG → PDF-based answers, LLM → normal chatbot
# -----------------------
mode = st.sidebar.radio(
    "Choose Mode",
    ["📄 PDF Chat (RAG)", "💬 General Chat"]
)

# -----------------------
# SESSION MEMORY              #to maintain chat history
# -----------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:               #loops through stored msgs
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------
# PDF UPLOAD SECTION
# -----------------------
pdf_text = None
chunks = None

if mode == "📄 PDF Chat (RAG)":
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        with open("temp.pdf", "wb") as f:                  #pdfreader works with file path. thus streamlit gives file in memory saves it locally as temp.pdf
            f.write(uploaded_file.getbuffer())

        pdf_text = load_pdf("temp.pdf")                #extracting text
        chunks = chunk_text(pdf_text)                  #chunking

        st.success(f"PDF loaded with {len(chunks)} chunks")

        if st.button("Index PDF into Vector DB"):         #UI for clearing old database and new chunks stored in chromaDB
            reset_db()
            store_chunks(chunks)
            st.success("PDF indexed successfully!")

# -----------------------
# CHAT INPUT
# -----------------------
query = st.chat_input("Ask something...")

if query:                   #runs only when user types something

    st.session_state.chat.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    # -----------------------
    # RAG MODE
    # -----------------------
    if mode == "📄 PDF Chat (RAG)":
        context_chunks = search(query)

        # DEBUG (optional)
        with st.expander("Retrieved context (debug)"):
            for i, c in enumerate(context_chunks):
                st.markdown(f"**Chunk {i+1}:** {c}")

        answer = generate_answer(query, context_chunks)

    # -----------------------
    # GENERAL MODE
    # -----------------------
    else:
        answer = generate_answer(query, None)

    st.session_state.chat.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)
    
    
