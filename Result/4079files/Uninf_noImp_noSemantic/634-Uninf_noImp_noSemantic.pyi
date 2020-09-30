from .parser import Definition
from collections import namedtuple
from typing import Any, Callable, Iterable, Optional

__all__: Any

ErrorParams = namedtuple('ErrorParams', ['code', 'short_desc', 'context'])

class Error:
    explain: bool = ...
    source: bool = ...
    code: Any = ...
    short_desc: Any = ...
    context: Any = ...
    parameters: Any = ...
    definition: Any = ...
    explanation: Any = ...
    def __init__(self, code: str, short_desc: str, context: str, *parameters: Iterable[str]) -> None: ...
    def set_context(self, definition: Definition, explanation: str) -> None: ...
    filename: Any = ...
    line: Any = ...
    @property
    def message(self) -> str: ...
    @property
    def lines(self) -> str: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: Error) -> bool: ...

class ErrorRegistry:
    groups: Any = ...
    class ErrorGroup:
        prefix: Any = ...
        name: Any = ...
        errors: Any = ...
        def __init__(self, prefix: str, name: str) -> None: ...
        def create_error(self, error_code: str, error_desc: str, error_context: Optional[str]=...) -> Callable[[Iterable[str]], Error]: ...
    @classmethod
    def create_group(cls: Any, prefix: str, name: str) -> ErrorGroup: ...
    @classmethod
    def get_error_codes(cls: Any) -> Iterable[str]: ...
    @classmethod
    def to_rst(cls: Any) -> str: ...

D1xx: Any
D100: Any
D101: Any
D102: Any
D103: Any
D104: Any
D105: Any
D106: Any
D107: Any
D2xx: Any
D200: Any
D201: Any
D202: Any
D203: Any
D204: Any
D205: Any
D206: Any
D207: Any
D208: Any
D209: Any
D210: Any
D211: Any
D212: Any
D213: Any
D214: Any
D215: Any
D3xx: Any
D300: Any
D301: Any
D302: Any
D4xx: Any
D400: Any
D401: Any
D401b: Any
D402: Any
D403: Any
D404: Any
D405: Any
D406: Any
D407: Any
D408: Any
D409: Any
D410: Any
D411: Any
D412: Any
D413: Any
D414: Any
D415: Any
D416: Any
D417: Any

class AttrDict(dict):
    def __getattr__(self, item: str) -> Any: ...

all_errors: Any
conventions: Any
