import ollama

def generate_answer(query, context_chunks=None):

    # --------------------------
    # MODE 1: GENERAL CHAT
    # --------------------------
    if not context_chunks:
        prompt = f"""
You are a helpful general AI assistant.

Answer normally and conversationally.

User: {query}
Assistant:
"""
    
    # --------------------------
    # MODE 2: RAG CHAT
    # --------------------------
    else:
        context = "\n\n".join(context_chunks)

        prompt = f"""
You are a precise technical assistant.

Use ONLY the context below.

If answer is not in context, say "Not found in document."

Context:
{context}

Question:
{query}

Answer (2–5 lines):
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]