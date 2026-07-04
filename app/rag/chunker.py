from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)


if __name__ == "__main__":
    from app.rag.loader import load_documents

    docs = load_documents()
    chunks = chunk_documents(docs)

    print(f"Loaded {len(docs)} pages")
    print(f"Created {len(chunks)} chunks")
    print(chunks[0].page_content[:300])