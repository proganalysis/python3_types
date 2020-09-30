# (generated with --quick)

from typing import Any, Dict

AdFocus: Any
AdfLy: Any
DEFAULT_HEADERS: Dict[str, str]
MetaRefresh: Any
ShorteSt: Any
UnshortenModule: Any
__version__: Any
requests: module

class UnshortenIt:
    _default_headers: Any
    _default_timeout: Any
    modules: dict
    def __init__(self, default_timeout = ..., default_headers = ...) -> None: ...
    def register_module(self, module) -> None: ...
    def register_modules(self, modules) -> None: ...
    def unshorten(self, uri, module = ..., timeout = ..., unshorten_nested = ..., force = ...) -> Any: ...
