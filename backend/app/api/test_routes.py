from fastapi import FastAPI
from app.api.test_generation_api import router

def register_test_routes(app: FastAPI):
    app.include_router(router)

