# Semantic Search

## Purpose

This document explains how semantic search is used in the Telecom AI NOC RAG Assistant.

Semantic search retrieves documents based on their meaning rather than matching exact keywords.

This enables more accurate retrieval of telecom knowledge for the RAG pipeline.

---

# Why Semantic Search?

Traditional keyword search looks for exact words.

Semantic search understands the meaning of the user's question.

Example

Question:

"What causes LOS?"

The system can retrieve documents containing:

- Loss of Signal
- Optical Signal Failure
- Fiber Cut
- Low Optical Power

even if the exact wording is different.

---

# Workflow

User Question

↓

Embedding Generation

↓

ChromaDB Vector Search

↓

Most Similar Documents

↓

Azure OpenAI

↓

AI Response

---

# Components

FastAPI

Receives the question.

Azure Embedding Model

Converts the question into a vector.

ChromaDB

Finds similar telecom documents.

Azure OpenAI

Generates the final response.

---

# Benefits

- Better retrieval accuracy
- Understands question meaning
- Reduces irrelevant results
- Improves AI response quality

---

# Example

Question

"Why do I have High BER?"

Retrieved Context

Documents discussing:

- Optical attenuation
- Low signal power
- Dirty connectors
- Fiber damage

Generated Answer

Azure OpenAI creates a structured troubleshooting response using the retrieved context.

---

# Files Used

app/rag/search.py

app/rag/embeddings.py

data/chromadb/

---

# Interview Questions

### What is semantic search?

Semantic search retrieves information based on meaning rather than exact keyword matching.

### Why is semantic search important in RAG?

It retrieves the most relevant document chunks before the language model generates the answer.

---

# Key Takeaways

- Semantic search improves retrieval quality.
- ChromaDB performs vector similarity search.
- Azure embeddings enable semantic matching.
- Better retrieval leads to better AI responses.