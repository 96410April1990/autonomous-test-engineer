from fastapi import FastAPI
from app.api.memory_api import router

def register_memory_routes(app:FastAPI):
    app.include_router(router)

