# Azure AI Foundry

## Purpose

Azure AI Foundry is Microsoft's unified platform for building, deploying and managing Artificial Intelligence applications.

In this project, Azure AI Foundry is used to create and manage the Azure OpenAI resources required by the Telecom AI NOC RAG Assistant.

---

# Why Azure AI Foundry?

Azure AI Foundry provides a central place to manage AI resources and services.

It simplifies the process of:

- Creating AI projects
- Deploying language models
- Managing AI resources
- Monitoring model usage
- Managing API access

---

# How It Is Used In This Project

Azure AI Foundry is used to:

- Create the Azure OpenAI resource.
- Deploy the Chat Model.
- Deploy the Embedding Model.
- Obtain API credentials.
- Manage model deployments.

The FastAPI application connects to these deployed models using environment variables stored in the `.env` file.

---

# Components Used

## Azure OpenAI Resource

Provides access to GPT models.

---

## Chat Model Deployment

Used to generate telecom responses.

---

## Embedding Model Deployment

Used to generate vector embeddings for semantic search.

---

## API Keys

Securely authenticate the application.

---

# Project Workflow

Azure AI Foundry

↓

Azure OpenAI Resource

↓

Chat Model

Embedding Model

↓

FastAPI Application

↓

Telecom AI NOC Assistant

---

# Environment Variables

The application connects to Azure AI Foundry using:

```text
AZURE_OPENAI_ENDPOINT

AZURE_OPENAI_API_KEY

AZURE_OPENAI_API_VERSION

AZURE_OPENAI_CHAT_DEPLOYMENT

AZURE_OPENAI_EMBEDDING_DEPLOYMENT
```

These values are stored in the `.env` file.

---

# Benefits

- Centralized AI management
- Enterprise-grade security
- Easy deployment of AI models
- Azure integration
- Scalable AI platform

---

# Limitations

- Requires an Azure subscription
- Requires internet connectivity
- Model usage may incur Azure costs depending on the subscription

---

# Files Used

.env

app/services/llm.py

app/rag/embeddings.py

requirements.txt

---

# Interview Questions

### What is Azure AI Foundry?

Azure AI Foundry is Microsoft's platform for creating, deploying and managing AI applications and models.

---

### Why did you use Azure AI Foundry?

It provides a managed way to deploy Azure OpenAI models and simplifies integration with enterprise applications.

---

### Is Azure AI Foundry the AI model?

No.

Azure AI Foundry is the management platform.

Azure OpenAI provides the AI models.

---

### How does your project use Azure AI Foundry?

The Telecom AI NOC RAG Assistant connects to Azure OpenAI model deployments created and managed through Azure AI Foundry.

---

# Key Takeaways

- Azure AI Foundry manages AI resources.
- Azure OpenAI provides the language models.
- FastAPI communicates with Azure OpenAI through Azure AI Foundry deployments.
- The platform simplifies model deployment and resource management.
- It is the cloud foundation for the AI capabilities used in this project.