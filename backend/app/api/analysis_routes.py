from fastapi import FastAPI

from app.api.analysis_api import router

def register_analysis_routes(app: FastAPI):
    app.include_router(router)
