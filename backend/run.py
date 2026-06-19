import uvicorn
from app.main import app
from app.startup_extension import initialize_app

initialize_app(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
