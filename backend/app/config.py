"""Application configuration via environment variables."""

from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """CareApp settings loaded from environment."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: str = Field(default="development", alias="ENVIRONMENT")
    database_url: str = Field(
        default="sqlite+aiosqlite:///./care_app.db",
        alias="DATABASE_URL",
    )
    database_echo: bool = Field(default=False, alias="DATABASE_ECHO")

    # LLM provider: gemini (default) or groq
    llm_provider: str = Field(default="gemini", alias="LLM_PROVIDER")
    gemini_api_key: str = Field(default="", alias="GEMINI_API_KEY")
    gemini_model: str = Field(default="gemini-flash-latest", alias="GEMINI_MODEL")
    groq_api_key: str = Field(default="", alias="GROQ_API_KEY")
    groq_model: str = Field(
        default="llama-3.3-70b-versatile",
        alias="GROQ_MODEL",
    )

    # Claude (commented for revert — set CLAUDE_API_KEY + LLM_PROVIDER=claude if restored)
    # claude_api_key: str = Field(default="", alias="CLAUDE_API_KEY")
    # claude_model: str = Field(
    #     default="claude-3-5-sonnet-20241022",
    #     alias="CLAUDE_MODEL",
    # )

    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    cors_origins: List[str] = Field(
        default=["http://localhost:5173", "http://localhost:3000"],
        alias="CORS_ORIGINS",
    )
    cors_allow_credentials: bool = Field(default=True, alias="CORS_ALLOW_CREDENTIALS")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    rate_limit_enabled: bool = Field(default=True, alias="RATE_LIMIT_ENABLED")
    rate_limit_requests: int = Field(default=100, alias="RATE_LIMIT_REQUESTS")
    rate_limit_seconds: int = Field(default=60, alias="RATE_LIMIT_SECONDS")
    app_name: str = "CareApp API"
    app_version: str = "0.1.0"

    @property
    def llm_provider_normalized(self) -> str:
        p = (self.llm_provider or "gemini").strip().lower()
        return p if p in ("gemini", "groq") else "gemini"

    @property
    def gemini_enabled(self) -> bool:
        return bool(self.gemini_api_key and self.gemini_api_key.strip())

    @property
    def groq_enabled(self) -> bool:
        return bool(self.groq_api_key and self.groq_api_key.strip())

    # @property
    # def claude_enabled(self) -> bool:
    #     return bool(self.claude_api_key and self.claude_api_key.strip())


@lru_cache
def get_settings() -> Settings:
    return Settings()
