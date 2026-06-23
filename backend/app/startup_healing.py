from fastapi import FastAPI

from app.api.routes import register_routes
from app.api.analysis_routes import register_analysis_routes
from app.api.test_routes import register_test_routes
from app.api.automation_routes import register_automation_routes
from app.api.execution_routes import register_execution_routes
from app.api.healing_routes import ( register_healing_routes )

def configure_app(app:FastAPI):
    register_routes(app)
    register_analysis_routes(app)
    register_test_routes(app)
    register_automation_routes(app)
    register_execution_routes(app)
    register_healing_routes(app)

    return app

