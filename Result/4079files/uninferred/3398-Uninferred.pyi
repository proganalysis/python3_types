from typing import Any

def create_app(match_headers: Any): ...
async def handler(request: Any): ...
async def test_https_middleware(aiohttp_client: Any, match_headers: Any, request_headers: Any, expected: Any) -> None: ...
