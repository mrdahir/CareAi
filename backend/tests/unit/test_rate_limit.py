"""Rate limit middleware unit tests."""

import pytest
from starlette.requests import Request

from app.middleware.rate_limit import RateLimitMiddleware


@pytest.mark.unit
def test_rate_limit_blocks_after_max():
    mw = RateLimitMiddleware(app=None, max_requests=2, window_seconds=60)
    assert mw._allow("127.0.0.1") is True
    assert mw._allow("127.0.0.1") is True
    assert mw._allow("127.0.0.1") is False


@pytest.mark.unit
def test_health_path_exempt():
    mw = RateLimitMiddleware(app=None, max_requests=1, window_seconds=60)
    assert mw._is_exempt("/api/health") is True
    assert mw._is_exempt("/api/chat") is False
