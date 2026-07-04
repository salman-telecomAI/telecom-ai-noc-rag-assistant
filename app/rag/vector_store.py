from chromadb import PersistentClient
from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.embeddings import embeddings

client = PersistentClient(path="data/chromadb")
collection = client.get_or_create_collection("telecom_docs")

docs = load_documents()
chunks = chunk_documents(docs)

#collection.delete(where={})

for i, chunk in enumerate(chunks):
    vector = embeddings.embed_query(chunk.page_content)

    collection.add(
        ids=[f"doc_{i}"],
        documents=[chunk.page_content],
        embeddings=[vector],
        metadatas=[chunk.metadata],
    )

print(f"Stored {len(chunks)} chunks in ChromaDB.")