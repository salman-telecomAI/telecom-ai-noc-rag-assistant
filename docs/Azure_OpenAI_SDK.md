# Azure OpenAI SDK

## Purpose

This document explains how the Azure OpenAI Python SDK is used in the Telecom AI NOC RAG Assistant.

The SDK enables the application to communicate with Azure OpenAI services for generating AI responses and creating embeddings for Retrieval-Augmented Generation (RAG).

---

# Why Azure OpenAI SDK?

The Azure OpenAI SDK provides a simple and secure way to access Azure-hosted AI models.

Benefits include:

- Secure API communication
- Chat completion support
- Embedding generation
- Easy integration with Python
- Reliable enterprise-grade AI service

---

# SDK Installation

Install the required package:

```bash
pip install openai
```

---

# Environment Variables

The SDK uses the following environment variables:

```text
AZURE_OPENAI_ENDPOINT

AZURE_OPENAI_API_KEY

AZURE_OPENAI_API_VERSION

AZURE_OPENAI_CHAT_DEPLOYMENT

AZURE_OPENAI_EMBEDDING_DEPLOYMENT
```

---

# SDK Workflow

User Question

↓

FastAPI

↓

Azure OpenAI SDK

↓

Azure OpenAI Service

↓

AI Response

---

# Chat Completion

The SDK sends the retrieved telecom context and user question to the Azure OpenAI Chat model.

The model generates a structured telecom response.

---

# Embedding Generation

The SDK converts telecom documents and user questions into vector embeddings.

These embeddings are stored in ChromaDB for semantic search.

---

# Files Using the SDK

app/services/llm.py

app/rag/embeddings.py

app/services/rag_service.py

---

# Advantages

- Easy Python integration
- Secure authentication
- Supports chat models
- Supports embedding models
- Reliable Azure service

---

# Interview Questions

### Why use the Azure OpenAI SDK?

It provides a simple and secure way to interact with Azure-hosted AI models from Python.

### What is the SDK used for in this project?

It generates embeddings and AI chat responses for the RAG pipeline.

---

# Key Takeaways

- The Azure OpenAI SDK connects the application to Azure AI services.
- It is used for chat completion and embedding generation.
- It is a core component of the RAG architecture.