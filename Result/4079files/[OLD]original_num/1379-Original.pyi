# (generated with --quick)

import abc
import enum
from typing import Any, Callable, List, Optional, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
Enum: Type[enum.Enum]
aiohttp: Any
asyncio: module
datetime: Type[datetime.datetime]
etree: Any
typing: module

_FuncT = TypeVar('_FuncT', bound=Callable)

class AndFilter(Filter):
    __doc__: str
    filters: List[Filter]
    def __init__(self, filters: List[Filter]) -> None: ...
    def generate_node(self, parent_node) -> Any: ...

class FieldFilter(Filter):
    __doc__: str
    name: Any
    operation: FilterOperation
    value: Any
    def __init__(self, operation: FilterOperation, name, value) -> None: ...
    def generate_node(self, parent_node) -> Any: ...

class FieldSort:
    __doc__: str
    _field: str
    _sort_order: SortOrder
    def __init__(self, field: str, sort_order: SortOrder) -> None: ...
    def to_string(self) -> str: ...

class Filter(metaclass=abc.ABCMeta):
    __doc__: str
    __metaclass__: Type[abc.ABCMeta]
    @abstractmethod
    def generate_node(self, parent_node) -> Any: ...

class FilterOperation(enum.Enum):
    __doc__: str
    equal: str
    exists: str
    greater_than: str
    greater_than_equal: str
    less_than: str
    less_than_equal: str
    like: str
    not_equal: str
    not_in: str
    not_like: str
    with_in: str

class NodeHelper(object):
    __doc__: str
    _node: Any
    def __init__(self, node) -> None: ...
    def get_bool(self, field) -> Any: ...
    def get_datetime(self, field) -> Optional[datetime.datetime]: ...
    def get_datetime_for_modified(self, field) -> Optional[datetime.datetime]: ...
    def get_text(self, field) -> Any: ...
    def get_texts(self, field) -> Optional[list]: ...

class OrFilter(Filter):
    __doc__: str
    filters: List[Filter]
    def __init__(self, filters: List[Filter]) -> None: ...
    def generate_node(self, parent_node) -> Any: ...

class SortOrder(enum.Enum):
    __doc__: str
    ascending: str
    decending: str

class Trafikverket(object):
    __doc__: str
    _api_key: str
    _api_url: str
    _client_session: Any
    date_time_format: str
    date_time_format_for_modified: str
    def __init__(self, client_session, api_key: str) -> None: ...
    def _generate_request_data(self, objecttype: str, includes: List[str], filters: List[Filter], limit: Optional[int] = ..., sorting: Optional[List[FieldSort]] = ...) -> Any: ...
    def async_make_request(self, objecttype: str, includes: List[str], filters: List[Filter], limit: Optional[int] = ..., sorting: Optional[List[FieldSort]] = ...) -> coroutine: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
