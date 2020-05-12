# (generated with --quick)

import collections
import functools
from typing import Any, Callable, Iterable, Iterator, Optional, Set, Sized, Tuple, Type, TypeVar, Union

ErrorParams = `namedtuple-ErrorParams-code-short_desc-context`

D100: Callable[[Iterable[str]], Error]
D101: Callable[[Iterable[str]], Error]
D102: Callable[[Iterable[str]], Error]
D103: Callable[[Iterable[str]], Error]
D104: Callable[[Iterable[str]], Error]
D105: Callable[[Iterable[str]], Error]
D106: Callable[[Iterable[str]], Error]
D107: Callable[[Iterable[str]], Error]
D1xx: Any
D200: Callable[[Iterable[str]], Error]
D201: Callable[[Iterable[str]], Error]
D202: Callable[[Iterable[str]], Error]
D203: Callable[[Iterable[str]], Error]
D204: Callable[[Iterable[str]], Error]
D205: Callable[[Iterable[str]], Error]
D206: Callable[[Iterable[str]], Error]
D207: Callable[[Iterable[str]], Error]
D208: Callable[[Iterable[str]], Error]
D209: Callable[[Iterable[str]], Error]
D210: Callable[[Iterable[str]], Error]
D211: Callable[[Iterable[str]], Error]
D212: Callable[[Iterable[str]], Error]
D213: Callable[[Iterable[str]], Error]
D214: Callable[[Iterable[str]], Error]
D215: Callable[[Iterable[str]], Error]
D2xx: Any
D300: Callable[[Iterable[str]], Error]
D301: Callable[[Iterable[str]], Error]
D302: Callable[[Iterable[str]], Error]
D3xx: Any
D400: Callable[[Iterable[str]], Error]
D401: Callable[[Iterable[str]], Error]
D401b: Callable[[Iterable[str]], Error]
D402: Callable[[Iterable[str]], Error]
D403: Callable[[Iterable[str]], Error]
D404: Callable[[Iterable[str]], Error]
D405: Callable[[Iterable[str]], Error]
D406: Callable[[Iterable[str]], Error]
D407: Callable[[Iterable[str]], Error]
D408: Callable[[Iterable[str]], Error]
D409: Callable[[Iterable[str]], Error]
D410: Callable[[Iterable[str]], Error]
D411: Callable[[Iterable[str]], Error]
D412: Callable[[Iterable[str]], Error]
D413: Callable[[Iterable[str]], Error]
D414: Callable[[Iterable[str]], Error]
D415: Callable[[Iterable[str]], Error]
D416: Callable[[Iterable[str]], Error]
D417: Callable[[Iterable[str]], Error]
D4xx: Any
Definition: Any
__all__: Tuple[str, str, str]
all_errors: Set[str]
conventions: AttrDict
is_blank: Any
partial: Type[functools.partial]

_T = TypeVar('_T')
_Tnamedtuple-ErrorParams-code-short_desc-context = TypeVar('_Tnamedtuple-ErrorParams-code-short_desc-context', bound=`namedtuple-ErrorParams-code-short_desc-context`)

class AttrDict(dict):
    def __getattr__(self, item: str) -> Any: ...

class Error:
    __doc__: str
    code: str
    context: str
    definition: Any
    explain: bool
    explanation: Optional[str]
    filename: Any
    line: Any
    lines: str
    message: str
    parameters: Tuple[Iterable[str], ...]
    short_desc: str
    source: bool
    def __init__(self, code: str, short_desc: str, context: str, *parameters: Iterable[str]) -> None: ...
    def __lt__(self, other: Error) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def set_context(self, definition, explanation: str) -> None: ...

class ErrorRegistry:
    ErrorGroup: type
    __doc__: str
    groups: list
    @classmethod
    def create_group(cls, prefix: str, name: str) -> Any: ...
    @classmethod
    def get_error_codes(cls) -> Iterable[str]: ...
    @classmethod
    def to_rst(cls) -> str: ...

class `namedtuple-ErrorParams-code-short_desc-context`(tuple):
    __slots__ = ["code", "context", "short_desc"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    code: Any
    context: Any
    short_desc: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-ErrorParams-code-short_desc-context`], code, short_desc, context) -> `_Tnamedtuple-ErrorParams-code-short_desc-context`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-ErrorParams-code-short_desc-context`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-ErrorParams-code-short_desc-context`: ...
    def _replace(self: `_Tnamedtuple-ErrorParams-code-short_desc-context`, **kwds) -> `_Tnamedtuple-ErrorParams-code-short_desc-context`: ...

def dropwhile(predicate: Callable[[_T], object], iterable: Iterable[_T]) -> Iterator[_T]: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
