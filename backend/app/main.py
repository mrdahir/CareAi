"""CareApp FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import chat, contraceptives, faq, health, myth_check, programme, recommend
from app.config import get_settings
from app.db.init_db import init_db
from app.logging_config import setup_logging
from app.middleware.error_handler import register_exception_handlers
from app.middleware.logging import RequestLoggingMiddleware
from app.middleware.rate_limit import maybe_add_rate_limit

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging(settings.log_level)
    await init_db()
    yield


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="CareApp — Reproductive health AI assistant for Sub-Saharan Africa",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(RequestLoggingMiddleware)
maybe_add_rate_limit(app)
register_exception_handlers(app)

api_prefix = "/api"
app.include_router(health.router, prefix=api_prefix)
app.include_router(chat.router, prefix=api_prefix)
app.include_router(recommend.router, prefix=api_prefix)
app.include_router(myth_check.router, prefix=api_prefix)
app.include_router(faq.router, prefix=api_prefix)
app.include_router(contraceptives.router, prefix=api_prefix)
app.include_router(programme.router, prefix=api_prefix)


@app.get("/")
async def root():
    return {
        "app": settings.app_name,
        "docs": "/docs",
        "health": f"{api_prefix}/health",
    }
