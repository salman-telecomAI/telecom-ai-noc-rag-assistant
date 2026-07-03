from fastapi import FastAPI

app = FastAPI(
    title="Telecom AI NOC RAG Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Telecom AI NOC RAG Assistant is running."
    }