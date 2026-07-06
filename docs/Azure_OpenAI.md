# Azure OpenAI

## Purpose

Azure OpenAI provides the Large Language Model (LLM) used by the Telecom AI NOC RAG Assistant to generate intelligent, structured and context-aware telecom responses.

Unlike a traditional chatbot, the AI model works together with Retrieval-Augmented Generation (RAG) to answer questions using the project's telecom knowledge base.

---

# Why Azure OpenAI?

This project uses Azure OpenAI because it provides secure, enterprise-grade access to OpenAI language models through Microsoft Azure.

Key advantages include:

- Enterprise security
- Reliable cloud service
- API-based integration
- High-quality language generation
- Embedding model support

---

# Models Used

## Chat Model

Purpose

Generates the final telecom response after receiving the retrieved context.

Example Questions

- What is LOS Alarm?
- Explain EDFA.
- What causes High BER?
- Explain Optical Power.

---

## Embedding Model

Purpose

Converts telecom documents and user questions into vector embeddings for semantic search.

These embeddings are stored inside ChromaDB.

---

# How Azure OpenAI Works

Application Flow

User Question

↓

FastAPI

↓

ChromaDB Search

↓

Relevant Telecom Context

↓

Azure OpenAI GPT

↓

Structured AI Response

---

# Environment Variables

Azure OpenAI requires the following configuration.

```text
AZURE_OPENAI_ENDPOINT

AZURE_OPENAI_API_KEY

AZURE_OPENAI_API_VERSION

AZURE_OPENAI_CHAT_DEPLOYMENT

AZURE_OPENAI_EMBEDDING_DEPLOYMENT
```

These values are stored inside the `.env` file and loaded when the application starts.

---

# Integration in This Project

Azure OpenAI is used in two places.

1. Embedding Generation

The embedding model converts telecom documents into vectors before they are stored in ChromaDB.

2. Response Generation

The chat model receives:

- User Question
- Retrieved Telecom Context
- System Prompt

It then generates a structured telecom answer.

---

# Benefits

- High-quality AI responses
- Enterprise-grade Azure service
- Easy integration with FastAPI
- Supports Retrieval-Augmented Generation (RAG)
- Reduces AI hallucinations when combined with ChromaDB

---

# Limitations

- Requires an Azure subscription
- Requires API configuration
- Internet connection required
- Usage may incur Azure costs depending on the subscription

---

# Files Used

app/services/llm.py

app/rag/embeddings.py

app/services/rag_service.py

.env

requirements.txt

---

# Interview Questions

### What is Azure OpenAI?

Azure OpenAI provides enterprise access to OpenAI language models through Microsoft Azure.

---

### Why use Azure OpenAI instead of the public OpenAI API?

Azure OpenAI offers enterprise security, Azure integration, resource management and compliance features while providing access to the same family of language models.

---

### Why are two models used?

The chat model generates responses.

The embedding model converts text into vectors for semantic search.

---

### How does Azure OpenAI work with RAG?

RAG first retrieves relevant telecom documents from ChromaDB.

Azure OpenAI then uses the retrieved context to generate a more accurate answer.

---

# Key Takeaways

- Azure OpenAI is the intelligence engine of this project.
- It works together with ChromaDB using Retrieval-Augmented Generation (RAG).
- The embedding model enables semantic search.
- The chat model generates structured telecom responses.
- Together they provide accurate, context-aware AI assistance for telecom engineers.