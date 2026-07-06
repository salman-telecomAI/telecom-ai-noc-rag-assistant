# REST API

## Purpose

The Telecom AI NOC RAG Assistant exposes its functionality through a REST API built using FastAPI.

The API allows users and applications to interact with the AI assistant by sending HTTP requests and receiving JSON responses.

The API is automatically documented using Swagger UI.

---

# Why REST API?

REST APIs provide a simple and standardized way for applications to communicate.

Using a REST API allows:

- Web applications
- Mobile applications
- Automation tools
- Network management systems
- Future front-end applications

to access the AI assistant.

---

# API Architecture

```text
User

↓

HTTP Request

↓

FastAPI

↓

RAG Service

↓

ChromaDB

↓

Azure OpenAI

↓

JSON Response
```

---

# Base URL

Local Development

```text
http://127.0.0.1:8000
```

Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# Available Endpoints

## GET /

Purpose

Returns a welcome message indicating that the API is running.

Example Request

```http
GET /
```

Example Response

```json
{
  "message": "Telecom AI NOC RAG Assistant Running"
}
```

---

## GET /health

Purpose

Checks the health status of the application.

Example Request

```http
GET /health
```

Example Response

```json
{
  "status": "healthy"
}
```

---

## POST /chat

Purpose

Accepts a telecom question and returns an AI-generated response.

Example Request

```http
POST /chat
```

Request Body

```json
{
    "question": "What is LOS Alarm?"
}
```

Example Response

```json
{
    "question": "What is LOS Alarm?",
    "answer": "...",
    "context": [
        "...",
        "...",
        "..."
    ]
}
```

---

# API Workflow

1. User submits a question.
2. FastAPI receives the request.
3. RAG Service searches ChromaDB.
4. Relevant document chunks are retrieved.
5. Azure OpenAI generates the answer.
6. JSON response is returned.

---

# Response Format

Each successful request returns:

- User Question
- AI Generated Answer
- Retrieved Context

This makes the response easy to inspect during development and debugging.

---

# HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Request successful |
| 400 | Invalid request |
| 500 | Internal server error |

---

# Testing the API

Start the application

```bash
uvicorn app.api:app --reload
```

Open Swagger

```text
http://127.0.0.1:8000/docs
```

Test the following endpoints:

- GET /
- GET /health
- POST /chat

---

# Files Used

app/api.py

app/services/rag_service.py

app/services/llm.py

---

# Interview Questions

### Why did you choose FastAPI?

FastAPI provides high performance, automatic API documentation, request validation and an easy development experience.

---

### What format does your API use?

The API uses JSON for both requests and responses.

---

### How can someone test your API?

Using Swagger UI at:

http://127.0.0.1:8000/docs

or any HTTP client such as Postman.

---

### What happens when a user calls POST /chat?

The request is processed by FastAPI, the RAG service retrieves relevant telecom information from ChromaDB, Azure OpenAI generates the answer and the API returns a JSON response.

---

# Key Takeaways

- FastAPI provides the REST API layer.
- Swagger UI enables interactive testing.
- JSON is used for request and response data.
- The API connects users with the RAG pipeline.
- The REST API is the main interface to the Telecom AI NOC RAG Assistant.