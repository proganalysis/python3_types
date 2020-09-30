# (generated with --quick)

from typing import Any, Tuple

__all__: Tuple[str, str, str]
json: module

class BackendAPIError(BackendError):
    __doc__: str
    data: Any
    reason: Any
    status: Any
    def __init__(self, status, reason, data) -> None: ...

class BackendClientError(BackendError):
    __doc__: str

class BackendError(Exception):
    __doc__: str
