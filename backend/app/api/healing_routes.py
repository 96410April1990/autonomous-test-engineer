from fastapi import FastAPI

from app.api.healing_api import router

def register_healing_routes(app:FastAPI):
    app.include_router(router)

