# Chat API

## Purpose

This document explains how the `/chat` endpoint works in the Telecom AI NOC RAG Assistant.

The Chat API is the main interface used by users to ask telecom-related questions and receive AI-generated responses.

---

# Endpoint

```http
POST /chat
```

---

# Request Format

Example Request

```json
{
    "question":"What is LOS Alarm?"
}
```

---

# Processing Workflow

User Question

↓

FastAPI

↓

RAG Service

↓

ChromaDB Retrieval

↓

Azure OpenAI

↓

JSON Response

---

# Response Format

Example Response

```json
{
    "question":"What is LOS Alarm?",
    "answer":"...",
    "context":[
        "...",
        "...",
        "..."
    ]
}
```

---

# Response Structure

The AI response typically includes:

- Definition
- Possible Causes
- Troubleshooting Steps
- Recommended Action

---

# Example Questions

- What is EDFA?
- Explain LOS Alarm.
- What causes High BER?
- What is Optical Power?
- Explain Fiber Cut Alarm.

---

# Error Handling

Possible errors include:

- Invalid request
- Missing question
- Azure OpenAI connection issue
- Internal server error

---

# Files Used

app/api.py

app/services/rag_service.py

---

# Interview Questions

### What does the Chat API do?

It accepts telecom questions, retrieves relevant information using RAG and returns an AI-generated response.

### Why use a POST request?

Because the user submits data (the question) in the request body.

---

# Key Takeaways

- `/chat` is the primary endpoint of the application.
- It combines FastAPI, ChromaDB and Azure OpenAI.
- Responses are returned in JSON format.