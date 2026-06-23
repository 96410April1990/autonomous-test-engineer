from fastapi import FastAPI
from app.api.automation_api import router

def register_automation_routes(app: FastAPI):
    app.include_router(router)

