from fastapi import APIRouter
from app.agents.playwright_generator_agent import ( PlaywrightGeneratorAgent )

router = APIRouter(prefix="/automation")
agent = PlaywrightGeneratorAgent()

@router.post("/generate")
def generate_playwright(test_case: dict):
    code = agent.generate_code(str(test_case))

    return { "generated_code": code }

