# (generated with --quick)

from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar

Column: Any
DBBASE: Any
Integer: Any
String: Any
__author__: str
collections: module

_Tnamedtuple-Query-query_id-query_name-query_length = TypeVar('_Tnamedtuple-Query-query_id-query_name-query_length', bound=`namedtuple-Query-query_id-query_name-query_length`)

class Query(Any):
    __doc__: str
    __tablename__: str
    named_tup: Type[`namedtuple-Query-query_id-query_name-query_length`]
    query_id: Any
    query_length: Any
    query_name: Any
    def __init__(self, name, length) -> None: ...
    def as_tuple(self) -> `namedtuple-Query-query_id-query_name-query_length`: ...

class `namedtuple-Query-query_id-query_name-query_length`(tuple):
    __slots__ = ["query_id", "query_length", "query_name"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    query_id: Any
    query_length: Any
    query_name: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Query-query_id-query_name-query_length`], query_id, query_name, query_length) -> `_Tnamedtuple-Query-query_id-query_name-query_length`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Query-query_id-query_name-query_length`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Query-query_id-query_name-query_length`: ...
    def _replace(self: `_Tnamedtuple-Query-query_id-query_name-query_length`, **kwds) -> `_Tnamedtuple-Query-query_id-query_name-query_length`: ...
