# Sequence Diagram

## Request Sequence

User
│
├── Submit Question
▼
FastAPI Backend
│
├── Send Query
▼
RAG Engine
│
├── Search Documents
▼
Vector Database
│
├── Return Relevant Documents
▼
RAG Engine
│
├── Build Prompt
▼
Azure OpenAI
│
├── Generate Response
▼
FastAPI Backend
│
└── Return Response
▼
User

## Purpose

The Sequence Diagram illustrates the order of interactions between the user, application components, vector database, and Azure OpenAI during a request.