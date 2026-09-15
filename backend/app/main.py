from fastapi import FastAPI

app = FastAPI(title="PathWise API")


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "PathWise API is running"
    }