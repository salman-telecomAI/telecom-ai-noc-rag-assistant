# REST API Design

## Objective

Provide REST endpoints for interacting with the Telecom AI NOC RAG Assistant.

## Endpoints

GET /
Returns application status.

GET /health
Returns application health.

POST /chat
Accepts a user question and returns an AI-generated response.

## Architecture

Client
↓
REST API
↓
FastAPI
↓
RAG Engine
↓
Azure OpenAI

## Benefits

- Standard API interface
- Easy integration
- Enterprise-ready
- Cloud-native

## Expected Outcome

A REST API that exposes the AI assistant to web, mobile and enterprise applications.