# (generated with --quick)

from typing import Any, Tuple, Type

KinesisRecord: Any
abc: module
datetime: Type[datetime.datetime]
typechecked: Any

class Bucket(abc.ABC, object):
    __doc__: str
    @abstractmethod
    def add(self, record) -> Any: ...
    @abstractmethod
    def flush(self) -> Any: ...
    @abstractmethod
    def get(self, force = ...) -> Any: ...

class InMemoryBucket(Bucket):
    _InMemoryBucket__count: int
    _InMemoryBucket__count_limit: Any
    _InMemoryBucket__data: list
    _InMemoryBucket__size_limit: Any
    get: Any
    def _InMemoryBucket__get(self) -> Tuple[list, nothing, nothing]: ...
    def __init__(self, size_limit, count_limit) -> None: ...
    def add(self, record) -> None: ...
    def flush(self) -> None: ...
