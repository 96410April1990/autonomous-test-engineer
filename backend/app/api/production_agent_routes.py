from fastapi import FastAPI
from app.api.production_agent_api import router

def register_production_agent_routes(app:FastAPI):
    app.include_router(router)