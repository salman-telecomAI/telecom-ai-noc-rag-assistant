from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Telecom AI NOC RAG Assistant",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "message": "Telecom AI NOC RAG Assistant is running."
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "application": "Telecom AI NOC RAG Assistant"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "question": request.question,
        "answer": "Placeholder AI response."
    }