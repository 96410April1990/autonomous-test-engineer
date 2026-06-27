from fastapi import APIRouter
from pydantic import BaseModel
from app.orchestrator.qa_orchestrator import ( QAOrchestrator )
from app.guardrails.qa_guardrails import ( QAGuardrail )

router = APIRouter(prefix="/agent")
agent = QAOrchestrator()
guardrail = QAGuardrail()

class AgentRequest(BaseModel):
    requirement:str

@router.post("/run")
def run_agent(request:AgentRequest):
    if not guardrail.validate_input(request.requirement):
        return { "error": "Requirement rejected by QA guardrail." }
    return agent.run(request.requirement)