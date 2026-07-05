import os

from dotenv import load_dotenv
from chromadb import PersistentClient

from app.rag.embeddings import embeddings

load_dotenv()

client = PersistentClient(
    path=os.getenv(
        "CHROMA_DB_PATH",
        "data/chromadb"
    )
)

collection = client.get_collection(
    "telecom_docs"
)


def search_documents(question: str, top_k: int = 3):

    vector = embeddings.embed_query(question)

    results = collection.query(
        query_embeddings=[vector],
        n_results=top_k
    )

    return results["documents"][0]