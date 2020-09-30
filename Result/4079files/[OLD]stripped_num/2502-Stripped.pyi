# (generated with --quick)

from typing import Any, Callable, Coroutine

APIFactory: Any
Command: Any
asyncio: module
functools: module
test_request_returns_list: Callable
test_request_returns_single: Callable

class MockCode:
    def is_successful(self) -> bool: ...

class MockContext:
    def request(self, arg) -> MockProtocol: ...

class MockProtocol:
    response: Any
    def mock_response(self) -> Coroutine[Any, Any, MockResponse]: ...

class MockResponse:
    code: MockCode
    payload: bytes

def async_test(f) -> Callable: ...
def mock_create_context(loop) -> Coroutine[Any, Any, MockContext]: ...
