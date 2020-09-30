# (generated with --quick)

import abc
from typing import Any, Callable, NoReturn, Sequence, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]

_FuncT = TypeVar('_FuncT', bound=Callable)

class Cacheable(metaclass=abc.ABCMeta):
    _allow_caching: bool

class HexSerializable(Hexlifiable, Serializable):
    def hexlify(self) -> str: ...

class Hexlifiable(metaclass=abc.ABCMeta):
    @abstractmethod
    def hexlify(self) -> Any: ...

class Immutable(Cacheable):
    def __delattr__(self, item) -> NoReturn: ...
    def __setattr__(self, key, value) -> NoReturn: ...

class Jsonizable(metaclass=abc.ABCMeta):
    @classmethod
    @abstractmethod
    def from_json(cls, string) -> Any: ...
    @abstractmethod
    def to_json(self) -> Any: ...

class Mutable(Uncacheable):
    def __delattr__(self, item) -> None: ...
    def __setattr__(self, key, value) -> None: ...

class Serializable(metaclass=abc.ABCMeta):
    @abstractmethod
    def serialize(self) -> Any: ...

class Uncacheable(metaclass=abc.ABCMeta):
    _allow_caching: bool

def abstractmethod(callable: _FuncT) -> _FuncT: ...
def cached(method) -> Callable: ...
def hexlify(data: bytes) -> bytes: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
