from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.qa_memory_agent import ( QAMemoryAgent )

router = APIRouter(prefix="/memory")
agent = QAMemoryAgent()

class MemoryRequest(BaseModel):
    issue:str
    solution:str

@router.post("/save")
def save_memory(request:MemoryRequest):
    return agent.remember(request.issue, request.solution)

@router.get("/search")
def search_memory(query:str):
    return agent.recall(query)

