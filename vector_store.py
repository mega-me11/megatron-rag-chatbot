print("🔥 LOADING VECTOR_STORE FROM:", __file__)
import chromadb
from utils.embeddings import get_embedding

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="pdf_chunks")

# -----------------------
# RESET DB
# -----------------------
def reset_db():
    global client, collection
    try:
        client.delete_collection("pdf_chunks")
    except:
        pass

    collection = client.get_or_create_collection(name="pdf_chunks")

# -----------------------
# STORE
# -----------------------
def store_chunks(chunks):
    embeddings = []

    for i, chunk in enumerate(chunks):
        embeddings.append(get_embedding(chunk))

    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings
    )

# -----------------------
# SEARCH
# -----------------------
def search(query, k=3):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    docs = results["documents"][0]

    return [doc.strip() for doc in docs if len(doc.strip()) > 20]