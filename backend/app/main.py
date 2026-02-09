from fastapi import FastAPI

app = FastAPI(title="DocDrop AI API")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello, World!"}

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

