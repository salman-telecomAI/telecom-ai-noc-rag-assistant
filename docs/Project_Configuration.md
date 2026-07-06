# Project Configuration

## Purpose

This document describes the configuration required to run the Telecom AI NOC RAG Assistant.

The project uses environment variables to securely store Azure OpenAI credentials and application settings.

---

# Configuration Overview

The application consists of the following configuration components:

- Python Virtual Environment
- Environment Variables
- Azure OpenAI
- ChromaDB
- FastAPI
- Logging

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```text
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/

AZURE_OPENAI_API_KEY=YOUR_API_KEY

AZURE_OPENAI_API_VERSION=2025-04-01-preview

AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4o

AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small

CHROMA_DB_PATH=data/chromadb

LOG_LEVEL=INFO
```

---

# Configuration Files

Project configuration is distributed across the following files:

```text
.env
requirements.txt
Dockerfile
.gitignore
.dockerignore
app/core/config.py
```

---

# Python Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Start Application

```bash
uvicorn app.api:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Docker Configuration

Build:

```bash
docker build -t telecom-ai-rag .
```

Run:

```bash
docker run -p 8000:8000 telecom-ai-rag
```

---

# Logging

Logging is enabled to record:

- Application startup
- API requests
- Retrieval operations
- Azure OpenAI requests
- Errors

---

# Security Notes

Never commit:

- .env
- API Keys
- Azure credentials

Sensitive information should always remain outside the Git repository.

---

# Configuration Checklist

- Python installed
- Virtual environment created
- Dependencies installed
- Azure OpenAI configured
- ChromaDB initialized
- FastAPI running
- Swagger accessible

---

# Key Takeaways

- Configuration is managed through environment variables.
- Secrets are excluded from Git using `.gitignore`.
- The application can run locally or inside Docker with the same configuration.