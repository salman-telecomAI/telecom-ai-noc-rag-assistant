# Embeddings

## Purpose

Embeddings convert text into numerical vectors that computers can compare mathematically.

In the Telecom AI NOC RAG Assistant, embeddings enable semantic search by representing telecom documents and user questions as vectors.

Without embeddings, Retrieval-Augmented Generation (RAG) would not be possible.

---

# Why Embeddings are Used

Traditional keyword search only matches exact words.

Example

Question

"What causes LOS?"

A keyword search may not find documents containing:

- Loss of Signal
- Optical Signal Failure
- Receive Signal Loss

Embeddings solve this problem by understanding the meaning of text instead of matching exact words.

---

# How Embeddings Work

Step 1

Telecom documents are loaded.

↓

Step 2

Documents are divided into small chunks.

↓

Step 3

Each chunk is converted into an embedding using Azure OpenAI.

↓

Step 4

Embeddings are stored inside ChromaDB.

↓

Step 5

A user asks a question.

↓

Step 6

The question is converted into another embedding.

↓

Step 7

ChromaDB compares vectors.

↓

Step 8

The most similar telecom documents are returned.

---

# Example

Document

"Loss of Signal (LOS) occurs when the receiver cannot detect an incoming optical signal."

Question

"Why do I have an LOS alarm?"

Although the wording is different, the embeddings identify that both texts have the same meaning.

The document is retrieved and sent to Azure OpenAI.

---

# Embedding Workflow

Telecom Documents

↓

Azure OpenAI Embedding Model

↓

Vector Embeddings

↓

ChromaDB

↓

Semantic Search

↓

Relevant Context

↓

Azure OpenAI Chat Model

↓

AI Response

---

# Azure Embedding Model

This project uses the Azure OpenAI Embedding Deployment.

Purpose

Convert text into vector embeddings.

The vectors are stored inside ChromaDB for semantic search.

---

# Benefits

• Understands meaning instead of exact words

• Improves search accuracy

• Supports semantic similarity

• Reduces incorrect document retrieval

• Essential for Retrieval-Augmented Generation (RAG)

---

# Limitations

• Requires an embedding model

• Embeddings must be regenerated if documents change significantly

• Very large datasets require more storage

---

# Files Used

app/rag/embeddings.py

app/rag/search.py

app/services/rag_service.py

data/chromadb/

requirements.txt

---

# Interview Questions

### What is an embedding?

An embedding is a numerical representation of text that captures its meaning.

---

### Why are embeddings important?

They allow semantic search by comparing meanings rather than exact words.

---

### Where are embeddings stored?

Embeddings are stored inside ChromaDB.

---

### Which model creates the embeddings?

The Azure OpenAI Embedding Model.

---

### How do embeddings improve AI responses?

They retrieve the most relevant telecom documents before Azure OpenAI generates the final answer.

---

# Key Takeaways

• Embeddings convert text into vectors.

• Similar meanings produce similar vectors.

• ChromaDB stores these vectors.

• Embeddings enable semantic search.

• Embeddings are a core component of the RAG architecture.