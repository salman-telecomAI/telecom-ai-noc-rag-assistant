# Deployment

## Purpose

This document explains how to deploy and run the Telecom AI NOC RAG Assistant.

The project supports local deployment using Python and Docker. The Docker image can also be pushed to Azure Container Registry (ACR) for future cloud deployment.

---

# Deployment Options

The application supports the following deployment methods:

- Local Python Environment
- Docker Container
- Azure Container Registry (Image Storage)

---

# Prerequisites

Install the following software before deployment:

- Python 3.11 or later
- Git
- Docker Desktop
- Visual Studio Code (Recommended)

---

# Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/telecom-ai-noc-rag-assistant.git
```

Move into the project folder.

```bash
cd telecom-ai-noc-rag-assistant
```

---

# Local Deployment

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a file named:

```text
.env
```

Add the required Azure OpenAI settings.

```text
AZURE_OPENAI_ENDPOINT=

AZURE_OPENAI_API_KEY=

AZURE_OPENAI_API_VERSION=

AZURE_OPENAI_CHAT_DEPLOYMENT=

AZURE_OPENAI_EMBEDDING_DEPLOYMENT=
```

---

## Start the Application

```bash
uvicorn app.api:app --reload
```

---

## Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# Docker Deployment

## Build Docker Image

```bash
docker build -t telecom-ai-rag .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 telecom-ai-rag
```

---

## Verify Docker Deployment

Open:

```text
http://localhost:8000/docs
```

Verify:

- API is running
- Swagger loads successfully
- POST /chat works
- AI answers telecom questions

---

# Azure Container Registry (ACR)

The project supports storing the Docker image in Azure Container Registry.

Basic workflow:

```text
Docker Image

↓

Azure Container Registry

↓

Future Cloud Deployment
```

Note:

The image can be deployed to Azure App Service or another container hosting platform when the required Azure subscription resources are available.

---

# Deployment Verification

Confirm the following:

- Application starts successfully
- Swagger UI is accessible
- Health endpoint returns "healthy"
- Chat endpoint returns AI responses
- Docker container runs correctly

---

# Troubleshooting

## Docker Does Not Start

Verify Docker Desktop is running.

---

## FastAPI Does Not Start

Ensure the virtual environment is activated and dependencies are installed.

---

## Azure OpenAI Connection Error

Check the values in the `.env` file.

---

## No AI Response

Verify:

- ChromaDB contains indexed telecom documents.
- Azure OpenAI credentials are correct.
- Internet connection is available.

---

# Files Used

Dockerfile

requirements.txt

.env

app/api.py

app/services/

---

# Interview Questions

### How can this application be deployed?

It can be deployed locally using Python, containerized with Docker, and the Docker image can be stored in Azure Container Registry for future cloud deployment.

---

### Why use Docker?

Docker provides a consistent runtime environment and simplifies deployment across different systems.

---

### What is Azure Container Registry?

Azure Container Registry is a managed service for storing Docker images before deployment.

---

# Key Takeaways

- The application supports local deployment and Docker.
- Docker ensures consistent execution across environments.
- Azure Container Registry stores the Docker image for future cloud deployment.
- The deployment process is simple, repeatable and suitable for demonstration purposes.