# (generated with --quick)

from typing import Any, List, Optional

UnshortenFailed: Any
UnshortenModule: Any
copy: module
json: module
re: module
requests: module
time: module

class ShorteSt(Any):
    domains: List[str]
    name: str
    def __init__(self, headers: Optional[dict] = ..., timeout: int = ...) -> None: ...
    def unshorten(self, uri: str) -> str: ...
