from app.rag.search import collection
from app.rag.embeddings import embeddings
from app.services.llm import ask_llm

question = "What is a Loss of Signal alarm in DWDM?"

vector = embeddings.embed_query(question)

results = collection.query(
    query_embeddings=[vector],
    n_results=3
)

context = "\n\n".join(results["documents"][0])

prompt = f"""
You are a senior DWDM engineer.

Use ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

answer = ask_llm(prompt)

print("=" * 60)
print(answer)
print("=" * 60)