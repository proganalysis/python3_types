# (generated with --quick)

from typing import Any, Set

UnshortenFailed: Any
UnshortenModule: Any
copy: module
re: module

class AdFocus(Any):
    domains: Set[str]
    name: str
    def __init__(self, headers = ..., timeout = ...) -> None: ...
    def unshorten(self, uri) -> Any: ...
