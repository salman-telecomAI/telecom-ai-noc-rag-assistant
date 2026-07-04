from app.rag.loader import list_documents


def run_rag_pipeline(question: str):
    documents = list_documents()

    return {
        "question": question,
        "documents_found": len(documents),
        "status": "RAG pipeline initialized"
    }


if __name__ == "__main__":
    result = run_rag_pipeline("What is LOS Alarm?")
    print(result)