from fastapi import FastAPI
from pydantic import BaseModel

from app.core.security import validate_question
from app.services.rag_service import generate_answer

app = FastAPI(
    title="Telecom AI NOC RAG Assistant",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Telecom AI NOC RAG Assistant Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    question = validate_question(request.question)

    return generate_answer(question)