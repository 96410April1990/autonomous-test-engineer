from fastapi import APIRouter, UploadFile
import shutil
from app.services.document_service import DocumentService

router = APIRouter(prefix="/documents")
service = DocumentService()

@router.post("/upload")
async def upload_document(file: UploadFile):
    path = (f"./uploads/{file.filename}")
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = service.process_document(path)

    return {"filename": file.filename, "content": text}

