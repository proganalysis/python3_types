# (generated with --quick)

import collections
import functools
from typing import Any, Callable, Generator, Iterable, Iterator, Sized, Tuple, Type, TypeVar, Union

ErrorParams = `namedtuple-ErrorParams-code-short_desc-context`

D100: functools.partial[nothing]
D101: functools.partial[nothing]
D102: functools.partial[nothing]
D103: functools.partial[nothing]
D104: functools.partial[nothing]
D105: functools.partial[nothing]
D106: functools.partial[nothing]
D107: functools.partial[nothing]
D1xx: Any
D200: functools.partial[nothing]
D201: functools.partial[nothing]
D202: functools.partial[nothing]
D203: functools.partial[nothing]
D204: functools.partial[nothing]
D205: functools.partial[nothing]
D206: functools.partial[nothing]
D207: functools.partial[nothing]
D208: functools.partial[nothing]
D209: functools.partial[nothing]
D210: functools.partial[nothing]
D211: functools.partial[nothing]
D212: functools.partial[nothing]
D213: functools.partial[nothing]
D214: functools.partial[nothing]
D215: functools.partial[nothing]
D2xx: Any
D300: functools.partial[nothing]
D301: functools.partial[nothing]
D302: functools.partial[nothing]
D3xx: Any
D400: functools.partial[nothing]
D401: functools.partial[nothing]
D401b: functools.partial[nothing]
D402: functools.partial[nothing]
D403: functools.partial[nothing]
D404: functools.partial[nothing]
D405: functools.partial[nothing]
D406: functools.partial[nothing]
D407: functools.partial[nothing]
D408: functools.partial[nothing]
D409: functools.partial[nothing]
D410: functools.partial[nothing]
D411: functools.partial[nothing]
D412: functools.partial[nothing]
D413: functools.partial[nothing]
D414: functools.partial[nothing]
D415: functools.partial[nothing]
D416: functools.partial[nothing]
D417: functools.partial[nothing]
D4xx: Any
Definition: Any
__all__: Tuple[str, str, str]
all_errors: set
conventions: AttrDict
is_blank: Any
partial: Type[functools.partial]

_T = TypeVar('_T')
_Tnamedtuple-ErrorParams-code-short_desc-context = TypeVar('_Tnamedtuple-ErrorParams-code-short_desc-context', bound=`namedtuple-ErrorParams-code-short_desc-context`)

class AttrDict(dict):
    def __getattr__(self, item) -> Any: ...

class Error:
    __doc__: str
    code: Any
    context: Any
    definition: Any
    explain: bool
    explanation: Any
    filename: Any
    line: Any
    lines: str
    message: str
    parameters: tuple
    short_desc: Any
    source: bool
    def __init__(self, code, short_desc, context, *parameters) -> None: ...
    def __lt__(self, other) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def set_context(self, definition, explanation) -> None: ...

class ErrorRegistry:
    ErrorGroup: type
    __doc__: str
    groups: list
    @classmethod
    def create_group(cls, prefix, name) -> Any: ...
    @classmethod
    def get_error_codes(cls) -> Generator[Any, Any, None]: ...
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
