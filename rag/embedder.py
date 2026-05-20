from sentence_transformers import SentenceTransformer
import chromadb
import uuid

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_collection():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(name="research_docs")
    return collection

def add_documents(docs: list[str], ids: list[str]):
    collection = get_collection()
    # Generate unique IDs every time to avoid conflicts
    unique_ids = [f"{str(uuid.uuid4())}" for _ in docs]
    embeddings = model.encode(docs).tolist()
    collection.add(documents=docs, embeddings=embeddings, ids=unique_ids)
    print(f"Added {len(docs)} documents to ChromaDB")

def search_documents(query: str, n_results: int = 3):
    collection = get_collection()
    count = collection.count()
    if count == 0:
        return []
    query_embedding = model.encode([query]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=min(n_results, count))
    return results["documents"][0] if results["documents"] else []