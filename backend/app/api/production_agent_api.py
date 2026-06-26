from fastapi import APIRouter
from pydantic import BaseModel
from app.orchestrator.production_orchestrator import ( ProductionQAOrchestrator )

router = APIRouter(prefix="/production-agent")
agent = ProductionQAOrchestrator()

class AgentRequest(BaseModel):
    requirement:str

@router.post("/run")
def run_agent(request:AgentRequest):
    return agent.run(request.requirement)