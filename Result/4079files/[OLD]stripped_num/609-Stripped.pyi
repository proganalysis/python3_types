# (generated with --quick)

from typing import Any

class APIKeyError(Exception):
    msg: Any
    def __init__(self, msg) -> None: ...
    def __str__(self) -> Any: ...

class NoNetworkError(Exception): ...

class NotFoundError(Exception):
    word: Any
    def __init__(self, word) -> None: ...

class QueryError(Exception):
    status_code: Any
    word: Any
    def __init__(self, word, status_code) -> None: ...

class TimeoutError(Exception): ...

class UnexpectedError(Exception):
    def __init__(self) -> None: ...
