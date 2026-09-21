from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agents.controller import run_agent

app = FastAPI(title="ResearchMate Agentic RAG API", version="1.0.0")

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(request: QueryRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    return run_agent(request.question).model_dump()
