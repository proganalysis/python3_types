# (generated with --quick)

from typing import Any, Optional

sslyze: Any

class HttpRequestGenerator:
    DEFAULT_USER_AGENT: str
    HTTP_GET_FORMAT: str
    @classmethod
    def get_request(cls, host: str, user_agent: Optional[str] = ...) -> bytes: ...
