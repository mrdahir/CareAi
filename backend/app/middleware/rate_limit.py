"""In-memory sliding-window rate limiting per client IP."""

import time
from collections import defaultdict
from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from app.config import get_settings

_EXEMPT_PREFIXES = ("/api/health", "/docs", "/openapi.json", "/redoc", "/")


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Limit requests per IP within a rolling time window."""

    def __init__(self, app, max_requests: int, window_seconds: int) -> None:
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._hits: dict[str, list[float]] = defaultdict(list)

    def _client_key(self, request: Request) -> str:
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        if request.client:
            return request.client.host
        return "unknown"

    def _is_exempt(self, path: str) -> bool:
        return any(
            path == p or (p != "/" and path.startswith(p)) for p in _EXEMPT_PREFIXES
        )

    def _allow(self, key: str) -> bool:
        now = time.monotonic()
        cutoff = now - self.window_seconds
        hits = [t for t in self._hits[key] if t > cutoff]
        if len(hits) >= self.max_requests:
            self._hits[key] = hits
            return False
        hits.append(now)
        self._hits[key] = hits
        return True

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        if self._is_exempt(request.url.path):
            return await call_next(request)

        key = self._client_key(request)
        if not self._allow(key):
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Rate limit exceeded. Please try again later.",
                    "retry_after_seconds": self.window_seconds,
                },
            )
        return await call_next(request)


def maybe_add_rate_limit(app) -> None:
    settings = get_settings()
    if not settings.rate_limit_enabled:
        return
    app.add_middleware(
        RateLimitMiddleware,
        max_requests=settings.rate_limit_requests,
        window_seconds=settings.rate_limit_seconds,
    )
