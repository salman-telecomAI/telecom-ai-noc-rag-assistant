# ChromaDB

## Purpose

ChromaDB is the vector database used by the Telecom AI NOC RAG Assistant. It stores document embeddings so that the application can retrieve the most relevant telecom information before generating an AI response.

---

## Why ChromaDB is Used

Large Language Models (LLMs) do not automatically know the contents of company-specific documents.

Instead of sending every document to the AI model, ChromaDB stores vector embeddings that allow fast semantic search.

This enables Retrieval-Augmented Generation (RAG).

---

## How ChromaDB Works

1. Telecom documents are loaded into the application.
2. Documents are divided into smaller chunks.
3. Each chunk is converted into a vector embedding using Azure OpenAI Embeddings.
4. The embeddings are stored in ChromaDB.
5. When a user asks a question, the application searches ChromaDB.
6. The most relevant document chunks are retrieved.
7. The retrieved information is sent to Azure OpenAI.
8. Azure OpenAI generates a professional telecom response.

---

## Implementation in This Project

The Telecom AI NOC RAG Assistant uses ChromaDB to store embeddings generated from telecom knowledge documents.

The retrieval process is fully automatic and runs whenever a user submits a question through the FastAPI endpoint.

The retrieved context improves answer accuracy and reduces AI hallucinations.

---

## Project Workflow

User Question

↓

FastAPI

↓

Embedding Search

↓

ChromaDB

↓

Relevant Telecom Documents

↓

Azure OpenAI

↓

AI Response

---

## Benefits

• Fast document retrieval

• Semantic search instead of keyword matching

• Better AI accuracy

• Reduced hallucinations

• Scalable knowledge base

• Easy to update with new telecom documents

---

## Limitations

• Requires document embedding before searching

• Search quality depends on document quality

• Very large databases require additional optimization

---

## Files Used

app/rag/

data/chromadb/

app/services/rag_service.py

requirements.txt

---

## Interview Questions

Q. What is ChromaDB?

A vector database used to store document embeddings for semantic search.

Q. Why use ChromaDB?

To retrieve relevant telecom knowledge before sending context to the Large Language Model.

Q. What problem does ChromaDB solve?

It allows AI to answer using project-specific knowledge instead of relying only on its pre-trained knowledge.

---

## Key Takeaways

• ChromaDB stores document embeddings.

• It enables semantic document retrieval.

• It improves AI response accuracy.

• It is a core component of the RAG architecture.

• It allows the Telecom AI Assistant to answer using telecom documentation.