from fastapi import FastAPI
from app.api.routes import register_routes

def initialize_app(app:FastAPI):
    register_routes(app)
    return app
