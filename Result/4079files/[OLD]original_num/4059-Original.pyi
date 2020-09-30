# (generated with --quick)

from typing import Any, Tuple

__all__: Tuple[str, str, str]
json: module

class BackendAPIError(BackendError):
    __doc__: str
    data: Any
    reason: str
    status: int
    def __init__(self, status: int, reason: str, data) -> None: ...

class BackendClientError(BackendError):
    __doc__: str

class BackendError(Exception):
    __doc__: str
