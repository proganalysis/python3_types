# (generated with --quick)

from typing import Any, Callable, Dict, Sequence

OAuth: Any
endpoints: Any
requests: module

class Client:
    api: Any
    auth: Any
    prefix: str
    session: Any
    def __init__(self, auth, requests_session = ...) -> None: ...
    def _build_request(self, func) -> Callable: ...
    def headers(self) -> Dict[str, str]: ...
    def request(self, method, url, params = ..., payload = ...) -> Any: ...

def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
