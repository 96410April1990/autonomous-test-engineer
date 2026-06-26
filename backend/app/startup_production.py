from fastapi import FastAPI
from app.api.routes import register_routes
from app.api.production_agent_routes import ( register_production_agent_routes )

def configure_app(app:FastAPI):
    register_routes(app)
    register_production_agent_routes(app)

    return app

