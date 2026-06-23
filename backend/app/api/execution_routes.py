from fastapi import FastAPI
from app.api.execution_api import router

def register_execution_routes(app: FastAPI):
    app.include_router(router)

