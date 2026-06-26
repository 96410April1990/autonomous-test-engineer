from fastapi import APIRouter
from pydantic import BaseModel
from app.orchestrator.qa_orchestrator import ( QAOrchestrator )

router = APIRouter(prefix="/agent")
agent = QAOrchestrator()

class AgentRequest(BaseModel):
    requirement:str

@router.post("/run")
def run_agent(request:AgentRequest):
    return agent.run(request.requirement)

