# Retrieval Strategy

## Objective

Define how the Telecom AI NOC RAG Assistant retrieves relevant enterprise knowledge.

## Retrieval Workflow

User Question
↓
Embedding Model
↓
Vector Database
↓
Top-K Relevant Chunks
↓
Prompt Builder
↓
Azure OpenAI
↓
AI Response

## Retrieval Process

1. Receive user question.
2. Generate question embedding.
3. Perform semantic search.
4. Retrieve Top-K relevant document chunks.
5. Build prompt with retrieved context.
6. Generate AI response.

## Benefits

- Improved accuracy
- Context-aware responses
- Reduced hallucinations
- Faster troubleshooting

## Expected Outcome

An efficient retrieval mechanism that consistently provides relevant telecom knowledge to the Large Language Model before response generation.