from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings import get_settings

settings = get_settings()

app = FastAPI(title="DocDrop AI API")

# Allow the browser-based frontend (on a different origin) to call this API.
allowed_origins = [o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello, World!"}

@app.get("/health")
def health() -> dict[str, str]:
    # Note: we return non-sensitive config to prove env wiring works.
    return {"status": "ok", "env": settings.ENV}

