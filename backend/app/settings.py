from functools import lru_cache

from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized, validated configuration for the API.

    We load config from environment variables (and optionally from a local `.env`),
    so the same code runs locally + in production with different settings.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Required: we will use this for Supabase auth + API calls.
    SUPABASE_URL: HttpUrl

    # Optional, but useful to see in logs/health checks.
    ENV: str = "dev"

    # Comma-separated list of allowed origins for browsers (CORS).
    # Local dev default: Vite React runs on http://localhost:5173
    CORS_ORIGINS: str = "http://localhost:5173"

# Provide a single getter for the settings object to avoid re-parsing the env vars on each request.
@lru_cache
def get_settings() -> Settings:
    # Cache so we parse/validate env vars once per process.
    return Settings()

