import uvicorn
from app.main import app
#from app.startup_extension import configure_app
#from app.startup_tests import configure_app
#from app.startup_automation import configure_app
#from app.startup_execution import configure_app
#from app.startup_healing import configure_app
#from app.startup_memory import configure_app
#from app.startup_orchestrator import configure_app
#from app.startup_production import configure_app
from app.startup_final import configure_app

#initialize_app(app)
configure_app(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
