from chromadb import PersistentClient

from app.rag.loader import load_documents
from app.rag.chunker import chunk_documents
from app.rag.embeddings import embeddings

client = PersistentClient(path="data/chromadb")

COLLECTION_NAME = "telecom_docs"

# Delete old collection if it exists
try:
    client.delete_collection(COLLECTION_NAME)
    print("Old collection deleted.")
except Exception:
    print("No existing collection found.")

# Create a fresh collection
collection = client.create_collection(COLLECTION_NAME)

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
