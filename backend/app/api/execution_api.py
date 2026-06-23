from fastapi import APIRouter
from app.services.execution_service import ( ExecutionService )

router = APIRouter(prefix="/execution")
service = ExecutionService()

@router.post("/run")
def execute_tests(path: str):
    result = service.execute(path)

    return result