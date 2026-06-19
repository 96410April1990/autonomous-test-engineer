from fastapi import APIRouter, UploadFile
import shutil
from app.services.document_service import DocumentService
from app.agents.requirement_analyzer_agent import ( RequirementAnalyzerAgent )

router = APIRouter(prefix="/analysis")
agent = RequirementAnalyzerAgent()
service = DocumentService()

@router.post("/requirement")
def analyze_requirement(file: UploadFile):
    path = (f"./uploads/{file.filename}")
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = service.process_document(path)
    result = agent.analyze(text)

    return result



