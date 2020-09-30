# (generated with --quick)

from typing import Any, List, Optional, Type, TypeVar

colorize: Any
re: module

_TUrl = TypeVar('_TUrl', bound=Url)

class Url(str):
    __doc__: str
    _match_regexp: str
    components: List[Optional[str]]
    host: Optional[str]
    path: Optional[str]
    port: Optional[str]
    query: Optional[str]
    scheme: Optional[str]
    def __call__(self) -> str: ...
    def __init__(self, _) -> None: ...
    def __new__(cls: Type[_TUrl], url) -> _TUrl: ...
    def __str__(self) -> Any: ...
    def _raw_value(self) -> str: ...
