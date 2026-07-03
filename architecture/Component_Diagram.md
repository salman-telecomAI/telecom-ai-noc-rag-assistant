# Component Diagram

## Components

### User Interface
Allows engineers to submit telecom questions.

↓

### FastAPI Backend
Receives requests and manages the application workflow.

↓

### RAG Engine
Retrieves relevant telecom knowledge.

↓

### Azure AI Search / ChromaDB
Performs semantic search on indexed documents.

↓

### Azure OpenAI
Generates context-aware responses.

↓

### Telecom Knowledge Base
Stores:
- Huawei Manuals
- Nokia Manuals
- SOPs
- RCA Reports
- Alarm Guides
- Network Documentation

## Component Flow

User Interface
        │
        ▼
FastAPI Backend
        │
        ▼
RAG Engine
        │
        ▼
Azure AI Search / ChromaDB
        │
        ▼
Azure OpenAI
        │
        ▼
Response to User

## Purpose

The Component Diagram defines the internal building blocks of the Telecom AI NOC RAG Assistant and how they interact.