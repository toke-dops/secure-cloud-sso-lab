from fastapi import FastAPI

app = FastAPI(title="Secure Cloud SSO Lab")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}