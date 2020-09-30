# (generated with --quick)

import abc
from typing import Any, Callable, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
ArchiveView: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class ExtensionBasedVersion(Version):
    __doc__: str
    def detect(self, extension, first_line) -> Any: ...

class HeaderBasedVersion(Version):
    __doc__: str
    def detect(self, extension, first_line) -> Any: ...

class Version(metaclass=abc.ABCMeta):
    __doc__: str
    def __str__(self) -> Any: ...
    @abstractmethod
    def detect(self, extension, first_line) -> Any: ...
    @abstractmethod
    def find_offset_and_key(self, archive) -> Any: ...
    def postprocess(self, source, sink) -> None: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
