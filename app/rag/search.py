from chromadb import PersistentClient
from app.rag.embeddings import embeddings

client = PersistentClient(path="data/chromadb")
collection = client.get_collection("telecom_docs")

query = "What causes Loss of Signal alarm in DWDM?"

vector = embeddings.embed_query(query)

results = collection.query(
    query_embeddings=[vector],
    n_results=3
)

print("=" * 60)

for i, doc in enumerate(results["documents"][0]):
    print(f"\nResult {i+1}\n")
    print(doc[:700])
    print("\n" + "=" * 60)