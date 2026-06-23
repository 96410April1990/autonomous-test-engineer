from fastapi import APIRouter
from app.agents.test_architect_agent import ( TestArchitectAgent )

router = APIRouter(prefix="/tests")
agent = TestArchitectAgent()

@router.post("/generate")
def generate_tests(requirement: dict):
    result = agent.generate_tests(str(requirement))
    return result


