# megatron-rag-chatbot
Hybrid RAG chatbot built with Streamlit, Ollama (Llama 3), ChromaDB, and Sentence Transformers for PDF-based question answering and general AI chat.
# 🤖 Megatron RAG Chatbot 🤖

## Overview

This project is a Dual Mode AI Chatbot built using Python, Streamlit, ChromaDB, Sentence Transformers, and Ollama.

The chatbot supports two modes:

1. **PDF Chat (RAG Mode)** – Answers questions based on the contents of a PDF document.
2. **General Chat Mode** – Functions as a normal AI assistant using the Llama3 model running locally through Ollama.

The project demonstrates the complete Retrieval-Augmented Generation (RAG) pipeline, including document processing, chunking, embeddings, vector storage, similarity search, and LLM-based answer generation.

---

## Features

* Chat with PDF documents
* General-purpose AI chat
* Local Llama3 inference using Ollama
* ChromaDB vector database
* Semantic search using embeddings
* Streamlit web interface
* Session-based chat history

---

## Tech Stack

* Python
* Streamlit
* Ollama
* Llama3
* ChromaDB
* Sentence Transformers
* PyPDF2

---

## Project Structure

chatbot/

├── data/

│ └── sample.pdf

├── utils/

│ ├── pdf_reader.py

│ ├── chunking.py

│ ├── embeddings.py

│ ├── vector_store.py

│ └── llm.py

├── streamlit_app.py

├── app.py

└── requirements.txt

---

## How It Works

### PDF Chat (RAG Mode)

1. PDF is loaded and converted into text.
2. Text is split into smaller chunks.
3. Chunks are converted into embeddings.
4. Embeddings are stored in ChromaDB.
5. User query is converted into an embedding.
6. Similar chunks are retrieved using vector similarity search.
7. Retrieved context is sent to Llama3.
8. Llama3 generates an answer based on the document.

### General Chat Mode

1. User question is sent directly to Llama3.
2. Llama3 generates a response without using document retrieval.

---

## Installation

```bash
git clone <repository-url>

cd chatbot

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Install Ollama and pull Llama3:

```bash
ollama pull llama3
```

Run the application:

```bash
streamlit run streamlit_app.py
```

---

## Example Questions

### PDF Mode

* What is sensor drift?
* Summarize the paper.
* What causes drift in MOS sensors?

### General Chat Mode

* Explain machine learning.
* What is a black hole?
* Give me Python interview questions.

---

## Future Improvements

* Upload PDFs directly from the UI
* Support multiple PDFs
* Source citations for answers
* Conversational memory
* Improved chunking strategy
* Deploy on cloud platforms

---


## Learning Outcomes

Through this project, I learned:

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Embeddings and semantic search
* Local LLM deployment with Ollama
* Streamlit application development
* End-to-end AI application architecture

## Screenshots

### General Chat Mode

![General Chat](general_chat.png)

### PDF Chat Mode

![PDF Chat](pdf_chat.png)

## Author

Megha Chatterjee
