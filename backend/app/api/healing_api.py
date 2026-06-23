from fastapi import APIRouter
from pydantic import BaseModel

from app.healing.failure_analyzer_agent import ( FailureAnalyzerAgent )
from app.healing.locator_healer import ( LocatorHealer )

router = APIRouter(prefix="/healing")

analyzer = FailureAnalyzerAgent()
healer = LocatorHealer()

class FailureRequest(BaseModel):
    failure:str

class HealingRequest(BaseModel):
    code:str
    error:str

@router.post("/analyze")
def analyze_failure(request: FailureRequest):
    result = analyzer.analyze(request.failure)
    return result

@router.post("/fix")
def heal_locator(request: HealingRequest):
    result = healer.heal(request.code, request.error)
    return { "fixed_code": result }



    


