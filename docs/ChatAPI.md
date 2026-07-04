# Chat API

## Objective

Expose the Telecom AI NOC RAG Assistant through a REST API.

## Endpoint

POST /chat

## Request

{
  "question": "What is LOS Alarm?"
}

## Response

{
  "answer": "Placeholder response"
}

## Workflow

Client

↓

FastAPI

↓

Retriever

↓

LLM

↓

Response

## Expected Outcome

The application accepts telecom questions and returns AI-generated responses.