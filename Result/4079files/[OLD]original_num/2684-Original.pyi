# (generated with --quick)

import asyncio.locks
import collections
import typing
from typing import Any, Callable, Coroutine, Dict, Iterable, List, Optional, Sized, Tuple, Type, TypeVar, Union

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
    __slots__ = ["body", "concurrency", "encoding", "fast_mode", "features", "headers", "injection", "match_function", "method", "oob_app", "oob_details", "oob_host", "parameters", "semaphore", "session", "target_parameter", "url"]
    __dict__: collections.OrderedDict[str, Any]
    _field_defaults: collections.OrderedDict[str, Any]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
    body: Optional[bytes]
    common_characters: typing.Counter[nothing]
    common_strings: typing.Counter[nothing]
    concurrency: int
    encoding: Encoding
    fast_mode: bool
    features: Dict[str, bool]
    headers: Dict[str, str]
    injection: Injection
    match_function: Callable[[int, str], bool]
    method: str
    null_context: Any
    oob_app: Any
    oob_details: str
    oob_host: str
    parameters: Dict[str, str]
    semaphore: asyncio.locks.BoundedSemaphore
    session: Any
    start: Any
    start_oob_server: Any
    target_parameter: str
    target_parameter_value: Any
    url: str
    def __getnewargs__(self) -> Tuple[str, str, str, Dict[str, str], Callable[[int, str], bool], int, bool, Optional[bytes], Dict[str, str], Encoding, str, Any, Dict[str, bool], Injection, asyncio.locks.BoundedSemaphore, str, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TAttackContext], url: str, method: str, target_parameter: str, parameters: Dict[str, str], match_function: Callable[[int, str], bool], concurrency: int, fast_mode: bool, body: Optional[bytes], headers: Dict[str, str], encoding: Encoding, oob_details: str, session = ..., features: Dict[str, bool] = ..., injection: Injection = ..., semaphore: asyncio.locks.BoundedSemaphore = ..., oob_host: str = ..., oob_app = ...) -> _TAttackContext: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[_TAttackContext], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> _TAttackContext: ...
    def _replace(self: _TAttackContext, **kwds) -> _TAttackContext: ...

class Encoding(enum.Enum):
    FORM: str
    URL: str

class Injection(tuple):
    __slots__ = ["example", "name", "payload", "test_template_payloads"]
    __dict__: collections.OrderedDict[str, Union[Callable[[str, str], str], str, Iterable[Tuple[str, bool]]]]
    _field_defaults: collections.OrderedDict[str, Union[Callable[[str, str], str], str, Iterable[Tuple[str, bool]]]]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str, str]
    example: str
    name: str
    payload: Union[Callable[[str, str], str], str]
    test_template_payloads: Iterable[Tuple[str, bool]]
    def __call__(self, working, expression) -> str: ...
    def __getnewargs__(self) -> Tuple[str, str, Iterable[Tuple[str, bool]], Union[Callable[[str, str], str], str]]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TInjection], name: str, example: str, test_template_payloads: Iterable[Tuple[str, bool]], payload: Union[Callable[[str, str], str], str]) -> _TInjection: ...
    def _asdict(self) -> collections.OrderedDict[str, Union[Callable[[str, str], str], str, Iterable[Tuple[str, bool]]]]: ...
    @classmethod
    def _make(cls: Type[_TInjection], iterable: Iterable[Union[Callable[[str, str], str], str, Iterable[Tuple[str, bool]]]], new = ..., len: Callable[[Sized], int] = ...) -> _TInjection: ...
    def _replace(self: _TInjection, **kwds: Union[Callable[[str, str], str], str, Iterable[Tuple[str, bool]]]) -> _TInjection: ...
    def test_payloads(self, working_value) -> List[Tuple[str, bool]]: ...

def check(context: AttackContext, payload: str) -> Coroutine[Any, Any, bool]: ...
