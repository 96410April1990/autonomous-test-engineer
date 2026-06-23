from fastapi import FastAPI
from app.api.routes import register_routes
from app.api.analysis_routes import register_analysis_routes
from app.api.test_routes import register_test_routes

def configure_app(app: FastAPI):
    register_routes(app)
    register_analysis_routes(app)
    register_test_routes(app)

    return app
