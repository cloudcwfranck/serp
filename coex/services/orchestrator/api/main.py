from fastapi import FastAPI

app = FastAPI(title="Orchestrator")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    return {"status": "ready"}
