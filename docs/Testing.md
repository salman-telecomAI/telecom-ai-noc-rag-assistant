# Testing

## Purpose

This document describes the testing performed on the Telecom AI NOC RAG Assistant to verify that all major components function correctly.

Testing ensures the application is stable, reliable and ready for demonstration.

---

# Testing Objectives

The objectives of testing are to:

- Verify API functionality
- Verify Retrieval-Augmented Generation (RAG)
- Verify Azure OpenAI integration
- Verify ChromaDB retrieval
- Verify Docker deployment
- Verify end-to-end application workflow

---

# Test Environment

Operating System

Windows 11

Development Environment

Visual Studio Code

Programming Language

Python 3.11+

Framework

FastAPI

Vector Database

ChromaDB

Large Language Model

Azure OpenAI

Container Platform

Docker Desktop

---

# Test Cases

## Test Case 1

Objective

Verify FastAPI starts successfully.

Command

```bash
uvicorn app.api:app --reload
```

Expected Result

- Application starts successfully.
- No startup errors.
- Swagger UI becomes available.

Status

PASS

---

## Test Case 2

Objective

Verify Swagger UI.

Open

```text
http://127.0.0.1:8000/docs
```

Expected Result

- Swagger page loads.
- Endpoints are visible.
- Endpoints can be executed.

Status

PASS

---

## Test Case 3

Objective

Verify Health Endpoint.

Request

```http
GET /health
```

Expected Result

```json
{
  "status": "healthy"
}
```

Status

PASS

---

## Test Case 4

Objective

Verify Chat Endpoint.

Request

```http
POST /chat
```

Example

```json
{
    "question":"What is LOS Alarm?"
}
```

Expected Result

- AI returns a structured telecom response.
- Relevant context is retrieved.
- No API errors.

Status

PASS

---

## Test Case 5

Objective

Verify ChromaDB Retrieval.

Expected Result

Relevant telecom document chunks are retrieved before AI generates the answer.

Status

PASS

---

## Test Case 6

Objective

Verify Azure OpenAI.

Expected Result

Azure OpenAI successfully generates a response using the retrieved telecom context.

Status

PASS

---

## Test Case 7

Objective

Verify Docker Deployment.

Commands

```bash
docker build -t telecom-ai-rag .

docker run -p 8000:8000 telecom-ai-rag
```

Expected Result

- Docker image builds successfully.
- Container starts successfully.
- Swagger works.
- AI responses work.

Status

PASS

---

# Sample Test Questions

- What is EDFA?

- Explain LOS Alarm.

- What causes High BER?

- Explain Optical Power.

- What is DWDM?

- Explain OTDR.

---

# Test Results Summary

| Component | Status |
|-----------|--------|
| FastAPI | PASS |
| Swagger | PASS |
| Azure OpenAI | PASS |
| ChromaDB | PASS |
| RAG Pipeline | PASS |
| Docker | PASS |
| REST API | PASS |

---

# Known Limitations

Current testing does not include:

- Load testing
- Performance testing
- Security penetration testing
- Multi-user testing

These are outside the scope of the current portfolio project.

---

# Files Tested

app/api.py

app/services/

app/rag/

Dockerfile

requirements.txt

---

# Interview Questions

### How did you test the application?

I verified the REST API, RAG pipeline, Azure OpenAI integration, ChromaDB retrieval and Docker deployment using FastAPI Swagger UI and manual test cases.

---

### How do you know the RAG pipeline works?

The application retrieves relevant telecom document chunks before Azure OpenAI generates the final response.

This behaviour was verified using multiple telecom questions.

---

# Key Takeaways

- All core project components were tested successfully.
- The API functions correctly.
- Docker deployment works.
- Azure OpenAI integration works.
- ChromaDB retrieval works.
- The application is ready for demonstration and interview discussions.