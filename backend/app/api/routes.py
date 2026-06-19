from fastapi import FastAPI
from app.api.document_api import router

def register_routes(app:FastAPI):
    app.include_router(router)


