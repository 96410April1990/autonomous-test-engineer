from fastapi import FastAPI
from app.api.agent_api import router

def register_agent_routes(app:FastAPI):
    app.include_router(router)

