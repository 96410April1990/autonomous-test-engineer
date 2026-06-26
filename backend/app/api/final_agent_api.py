from fastapi import APIRouter
from pydantic import BaseModel
from app.orchestrator.final_orchestrator import ( FinalQAOrchestrator )

router = APIRouter(prefix="/qa-agent")
agent = FinalQAOrchestrator()

class QARequest(BaseModel):
    requirement:str

@router.post("/run")
def run(request: QARequest):
    return agent.run(request.requirement)

