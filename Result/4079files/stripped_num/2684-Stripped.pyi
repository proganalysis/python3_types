# (generated with --quick)

import asyncio.locks
import collections
import typing
from typing import Any, Callable, Iterable, List, Sized, Tuple, Type, TypeVar

BoundedSemaphore: Type[asyncio.locks.BoundedSemaphore]
ClientSession: Any
Counter: Type[typing.Counter]
TCPConnector: Any
asynccontextmanager: Any
create_app: Any
defaultdict: Type[collections.defaultdict]
enum: module
web: Any

_TAttackContext = TypeVar('_TAttackContext', bound=AttackContext)
_TInjection = TypeVar('_TInjection', bound=Injection)

class AttackContext(tuple):
    __slots__ = []
    __dict__: collections.OrderedDict[str, None]
    _field_defaults: collections.OrderedDict[str, None]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[nothing, ...]
    common_characters: typing.Counter[nothing]
    common_strings: typing.Counter[nothing]
    features: collections.defaultdict[nothing, bool]
    injection: None
    null_context: Any
    oob_app: None
    oob_host: None
    semaphore: None
    session: None
    start: Any
    start_oob_server: Any
    target_parameter_value: Any
    def __getnewargs__(self) -> Tuple[nothing, ...]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TAttackContext]) -> _TAttackContext: ...
    def _asdict(self) -> collections.OrderedDict[str, None]: ...
    @classmethod
    def _make(cls: Type[_TAttackContext], iterable: Iterable[None], new = ..., len: Callable[[Sized], int] = ...) -> _TAttackContext: ...
    def _replace(self: _TAttackContext, **kwds: None) -> _TAttackContext: ...

class Encoding(enum.Enum):
    FORM: str
    URL: str

class Injection(tuple):
    __slots__ = []
    __dict__: collections.OrderedDict[str, None]
    _field_defaults: collections.OrderedDict[str, None]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[nothing, ...]
    def __call__(self, working, expression) -> Any: ...
    def __getnewargs__(self) -> Tuple[nothing, ...]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TInjection]) -> _TInjection: ...
    def _asdict(self) -> collections.OrderedDict[str, None]: ...
    @classmethod
    def _make(cls: Type[_TInjection], iterable: Iterable[None], new = ..., len: Callable[[Sized], int] = ...) -> _TInjection: ...
    def _replace(self: _TInjection, **kwds: None) -> _TInjection: ...
    def test_payloads(self, working_value) -> List[Tuple[Any, Any]]: ...

def check(context, payload) -> coroutine: ...
