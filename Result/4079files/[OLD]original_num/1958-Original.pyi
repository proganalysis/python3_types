# (generated with --quick)

from typing import Any, Dict, Optional

AdFocus: Any
AdfLy: Any
DEFAULT_HEADERS: Dict[str, str]
MetaRefresh: Any
ShorteSt: Any
UnshortenModule: Any
__version__: Any
requests: module

class UnshortenIt:
    _default_headers: Optional[dict]
    _default_timeout: Optional[int]
    modules: dict
    def __init__(self, default_timeout: int = ..., default_headers: Optional[dict] = ...) -> None: ...
    def register_module(self, module) -> None: ...
    def register_modules(self, modules: list) -> None: ...
    def unshorten(self, uri: str, module: Optional[str] = ..., timeout: Optional[int] = ..., unshorten_nested: bool = ..., force: bool = ...) -> str: ...
