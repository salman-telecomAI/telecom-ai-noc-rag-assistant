# Telecom AI NOC RAG Assistant

An AI-powered Telecom Network Operations Center (NOC) assistant built using FastAPI, Azure OpenAI, ChromaDB and Retrieval-Augmented Generation (RAG).

The assistant helps telecom engineers answer technical questions using a telecom knowledge base and generates structured troubleshooting guidance for common network issues.

This project was developed as a professional portfolio project to demonstrate practical AI engineering skills for Telecom AI, Azure OpenAI and RAG-based applications.

---

# Project Overview

Telecom engineers often need quick access to accurate troubleshooting information during fault investigation.

Instead of manually searching through documents, this AI assistant retrieves the most relevant telecom knowledge and combines it with Azure OpenAI to generate clear, structured and easy-to-understand answers.

The application focuses on optical transport and telecom network operations while demonstrating modern AI architecture using Retrieval-Augmented Generation (RAG).

---

# Project Objectives

The objectives of this project are:

- Build an AI-powered Telecom NOC Assistant.
- Demonstrate Retrieval-Augmented Generation (RAG).
- Integrate Azure OpenAI with FastAPI.
- Store telecom knowledge in ChromaDB.
- Containerize the application using Docker.
- Create a professional GitHub portfolio project.
- Demonstrate AI engineering skills during interviews.

---

# Key Features

- AI-powered telecom troubleshooting assistant
- Retrieval-Augmented Generation (RAG)
- Azure OpenAI integration
- ChromaDB vector database
- FastAPI REST API
- Interactive Swagger API documentation
- Docker support
- Git version control
- Simple and modular project structure

---

# System Architecture

```text
                 User
                   │
                   ▼
             FastAPI API
                   │
                   ▼
            RAG Retrieval
                   │
                   ▼
             ChromaDB
                   │
                   ▼
          Azure OpenAI GPT
                   │
                   ▼
            AI Response
```

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| Azure OpenAI | Large Language Model |
| ChromaDB | Vector Database |
| Docker | Containerization |
| Git | Version Control |
| GitHub | Source Code Repository |
| VS Code | Development Environment |

---

# Project Folder Structure

```text
telecom-ai-noc-rag-assistant
│
├── app
│   ├── api.py
│   ├── core
│   ├── rag
│   ├── services
│   └── utils
│
├── architecture
├── config
├── data
├── docs
├── images
├── logs
├── prompts
├── scripts
├── tests
│
├── Dockerfile
├── requirements.txt
├── .env.example
├── .gitignore
├── .dockerignore
├── README.md
├── PROJECT_GUIDE.md
├── CHANGELOG.md
└── LICENSE
```

---

# How the Application Works

1. User submits a telecom question.
2. FastAPI receives the request.
3. ChromaDB searches the telecom knowledge base.
4. Relevant documents are retrieved.
5. Azure OpenAI receives the retrieved context.
6. AI generates a structured answer.
7. Response is returned to the user.

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/telecom-ai-noc-rag-assistant.git
```

Go to the project directory

```bash
cd telecom-ai-noc-rag-assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a file named

```text
.env
```

Add your Azure OpenAI configuration.

```text
AZURE_OPENAI_ENDPOINT=

AZURE_OPENAI_API_KEY=

AZURE_OPENAI_CHAT_DEPLOYMENT=

AZURE_OPENAI_EMBEDDING_DEPLOYMENT=
```

---

# Running the Application

Start FastAPI

```bash
uvicorn app.api:app --reload
```

Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

Health Check

```text
http://127.0.0.1:8000/health
```

---

# Docker

Build Docker Image

```bash
docker build -t telecom-ai-rag .
```

Run Docker Container

```bash
docker run -p 8000:8000 telecom-ai-rag
```

Open Swagger

```text
http://localhost:8000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| POST | /chat | Ask Telecom Questions |

---

# Example Questions

- What is EDFA?
- Explain LOS Alarm.
- What causes High BER?
- What is Optical Power?
- Explain Fiber Cut Alarm.
- What is OSNR?
- What is DWDM?
- Explain OTDR.
- How do you troubleshoot low receive power?
- What causes CRC errors?

---

# Example AI Response Format

Definition

Possible Causes

Troubleshooting Steps

Recommended Action

Related Commands (if applicable)

---

# Screenshots

Add screenshots inside the images folder.

Recommended screenshots:

- Project Folder Structure
- Swagger UI
- Chat Response
- Docker Running
- GitHub Repository
- Architecture Diagram

Example

```text
images/
    project-folder.png
    swagger-ui.png
    chat-response.png
    docker-running.png
    github-home.png
    architecture-diagram.png
```

---

# Current Project Status

Version: 1.0

Status:

Completed

- FastAPI API
- Azure OpenAI Integration
- ChromaDB Integration
- RAG Retrieval
- Docker Support
- GitHub Repository
- Swagger Documentation

---

# Future Improvements

Future enhancements may include:

- Authentication
- Multiple telecom knowledge bases
- Chat history
- User feedback
- Azure deployment
- CI/CD pipeline
- Monitoring and logging
- Role-based access control

---

# Learning Outcomes

This project demonstrates practical experience with:

- FastAPI
- Azure OpenAI
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- Docker
- GitHub
- AI Application Development
- Telecom AI Use Cases

---

# License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

# Author

Salman Shahid

Telecom AI | Azure AI | Network Automation

GitHub

https://github.com/YOUR_USERNAME

LinkedIn

https://www.linkedin.com/in/YOUR_PROFILE

---

# Acknowledgements

Special thanks to Microsoft Azure OpenAI, FastAPI, ChromaDB and the open-source community for providing the technologies used in this project.