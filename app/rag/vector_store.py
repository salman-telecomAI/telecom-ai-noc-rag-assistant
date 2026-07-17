from chromadb import PersistentClient

from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.embeddings import embeddings

client = PersistentClient(path="data/chromadb")

collection = client.get_or_create_collection("telecom_docs")

docs = load_documents()

chunks = chunk_documents(docs)

# Uncomment if rebuilding from scratch
# collection.delete(where={})

documents = []
ids = []
vectors = []
metadatas = []

for i, chunk in enumerate(chunks):

    documents.append(chunk.page_content)

    ids.append(f"doc_{i}")

    vectors.append(embeddings.embed_query(chunk.page_content))

    metadatas.append(chunk.metadata)

collection.add(
    ids=ids,
    documents=documents,
    embeddings=vectors,
    metadatas=metadatas,
)

print(f"Indexed {len(chunks)} chunks successfully.")
