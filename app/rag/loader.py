from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

DATA_DIR = Path("data")


def load_documents():
    documents = []

    pdf_files = pdf_files = pdf_files = DATA_DIR.rglob("*.pdf")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        docs = loader.load()

        for doc in docs:
            doc.metadata["source_file"] = pdf.name

        documents.extend(docs)

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print("=" * 60)
    print(f"Loaded {len(docs)} pages")

    if docs:
        print("=" * 60)
        print(docs[0].metadata)
        print("=" * 60)
        print(docs[0].page_content[:500])