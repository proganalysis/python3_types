# (generated with --quick)

from typing import Any, Optional, Tuple, Type

KinesisRecord: Any
abc: module
datetime: Type[datetime.datetime]
typechecked: Any

class Bucket(abc.ABC, object):
    __doc__: str
    @abstractmethod
    def add(self, record) -> None: ...
    @abstractmethod
    def flush(self) -> None: ...
    @abstractmethod
    def get(self, force: bool = ...) -> Tuple[list, Optional[str], Optional[datetime.datetime]]: ...

class InMemoryBucket(Bucket):
    _InMemoryBucket__count: int
    _InMemoryBucket__count_limit: int
    _InMemoryBucket__data: list
    _InMemoryBucket__size_limit: int
    get: Any
    def _InMemoryBucket__get(self) -> Tuple[list, nothing, nothing]: ...
    def __init__(self, size_limit: int, count_limit: int) -> None: ...
    def add(self, record) -> None: ...
    def flush(self) -> None: ...
