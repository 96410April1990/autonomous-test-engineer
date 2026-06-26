from fastapi import FastAPI
from app.api.final_agent_api import router

def register_final_routes(app:FastAPI):
    app.include_router(router)

