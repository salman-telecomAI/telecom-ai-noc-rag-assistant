from app.services.llm import ask_llm
from app.rag.search import collection
from app.rag.embeddings import embeddings

print("=" * 60)
print("Telecom AI NOC RAG Assistant")
print("Type 'exit' to quit")
print("=" * 60)

while True:
    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    vector = embeddings.embed_query(question)

    results = collection.query(
        query_embeddings=[vector],
        n_results=3
    )

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are a Senior DWDM/NOC Engineer.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_llm(prompt)

    print("\nAnswer:\n")
    print(answer)
    print("\n" + "=" * 60)