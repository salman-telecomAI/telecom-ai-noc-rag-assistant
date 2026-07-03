# Data Flow Diagram

## Flow

User Question
        │
        ▼
FastAPI Backend
        │
        ▼
RAG Engine
        │
        ▼
Vector Database (Azure AI Search / ChromaDB)
        │
        ▼
Relevant Telecom Documents
        │
        ▼
Azure OpenAI
        │
        ▼
Generated Response
        │
        ▼
FastAPI Backend
        │
        ▼
User

## Data Description

### Input
Natural language telecom question.

### Processing
Semantic search retrieves relevant enterprise documents.

### AI Processing
Azure OpenAI generates a context-aware answer using the retrieved documents.

### Output
Accurate telecom response with supporting document context.

## Purpose

The Data Flow Diagram explains how data travels through the Telecom AI NOC RAG Assistant from user input to AI-generated response.