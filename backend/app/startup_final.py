from fastapi import FastAPI
from app.api.final_agent_routes import ( register_final_routes )

def configure_app(app: FastAPI):
    register_final_routes(app)
    return app

