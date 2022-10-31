from typing import Any

def async_test(f: Any): ...

class MockCode:
    def is_successful(self): ...

class MockResponse:
    @property
    def code(self): ...
    @property
    def payload(self): ...

class MockProtocol:
    async def mock_response(self): ...
    @property
    def response(self): ...

class MockContext:
    def request(self, arg: Any): ...

async def mock_create_context(loop: Any): ...
async def test_request_returns_single(monkeypatch: Any) -> None: ...
async def test_request_returns_list(monkeypatch: Any) -> None: ...