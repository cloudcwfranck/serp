from fastapi import FastAPI

app = FastAPI(title="Translator")

@app.post("/translate")
def translate():
    return {"result": "ok"}
