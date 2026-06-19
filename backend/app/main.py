from fastapi import FastAPI

app = FastAPI(
    title="Autonomous Test Engineer Agent"
)

@app.get("/")
def health_check():
    return {
        "status": "Autonomous Test Engineer Agent up and running."
    }
