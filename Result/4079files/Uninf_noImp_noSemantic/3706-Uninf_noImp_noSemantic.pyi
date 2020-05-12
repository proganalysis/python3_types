from .auth import OAuth
from typing import Any, Optional

class Client:
    prefix: str = ...
    api: Any = ...
    session: Any = ...
    auth: Any = ...
    def __init__(self, auth: OAuth, requests_session: Any=...) -> None: ...
    def _build_request(self, func: Any): ...
    def headers(self): ...
    def request(self, method: Any, url: Any, params: Optional[Any] = ..., payload: Optional[Any] = ...): ...
