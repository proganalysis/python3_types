# (generated with --quick)

from typing import Any, Optional, Set

UnshortenFailed: Any
UnshortenModule: Any
copy: module
re: module

class AdFocus(Any):
    domains: Set[str]
    name: str
    def __init__(self, headers: Optional[dict] = ..., timeout: int = ...) -> None: ...
    def unshorten(self, uri: str) -> str: ...
