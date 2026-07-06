# Chunking

## Purpose

Chunking is the process of dividing large telecom documents into smaller, manageable sections called chunks.

These chunks are later converted into embeddings and stored in ChromaDB for semantic search.

Chunking improves retrieval accuracy and enables the AI assistant to retrieve only the most relevant information.

---

# Why It Is Used

Large documents cannot be efficiently searched as a single block of text.

If an entire document is embedded as one vector:

- Important details may be missed.
- Search accuracy decreases.
- AI receives unnecessary context.

Chunking solves these problems by creating smaller pieces of information that are easier to search and retrieve.

---

# How It Works

Step 1

Load telecom documents.

↓

Step 2

Split each document into smaller chunks.

↓

Step 3

Generate an embedding for each chunk.

↓

Step 4

Store the chunk embeddings in ChromaDB.

↓

Step 5

When a user asks a question, only the most relevant chunks are retrieved.

↓

Step 6

The retrieved chunks are sent to Azure OpenAI.

↓

Step 7

Azure OpenAI generates the final answer.

---

# Example

Original Document

"Loss of Signal (LOS) occurs when the receiver cannot detect an incoming optical signal. Common causes include fiber cuts, dirty connectors, failed transceivers and low optical power."

After Chunking

Chunk 1

"Loss of Signal (LOS) occurs when the receiver cannot detect an incoming optical signal."

Chunk 2

"Common causes include fiber cuts, dirty connectors, failed transceivers and low optical power."

Each chunk is stored separately and can be retrieved independently.

---

# Implementation in This Project

The Telecom AI NOC RAG Assistant splits telecom documentation into smaller text chunks before generating embeddings.

Each chunk becomes an individual searchable unit inside ChromaDB.

This allows the application to retrieve only the information that is most relevant to the user's question.

---

# Chunking Workflow

Telecom Document

↓

Chunking

↓

Multiple Text Chunks

↓

Embeddings

↓

ChromaDB

↓

Semantic Search

↓

Azure OpenAI

↓

AI Response

---

# Benefits

- Improves retrieval accuracy
- Reduces unnecessary context
- Faster semantic search
- Better AI responses
- Scalable for large knowledge bases

---

# Limitations

- Very small chunks may lose context.
- Very large chunks reduce search accuracy.
- Choosing the right chunk size is important for optimal results.

---

# Files Used

app/rag/

app/rag/embeddings.py

app/rag/search.py

data/

requirements.txt

---

# Interview Questions

### What is chunking?

Chunking is the process of dividing large documents into smaller sections before creating embeddings.

---

### Why is chunking important?

It improves semantic search by allowing the system to retrieve only the most relevant parts of a document.

---

### What happens after chunking?

Each chunk is converted into an embedding and stored in ChromaDB.

---

### Does chunk size affect search quality?

Yes.

Chunks that are too small may lose context, while chunks that are too large may reduce retrieval accuracy.

---

# Key Takeaways

- Chunking divides documents into smaller sections.
- Each chunk is embedded independently.
- Chunks are stored in ChromaDB.
- Chunking improves semantic retrieval.
- It is a fundamental step in the RAG pipeline.