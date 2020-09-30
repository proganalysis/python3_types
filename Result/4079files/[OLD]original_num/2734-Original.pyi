# (generated with --quick)

import abc
from typing import Any, BinaryIO, Callable, Optional, Tuple, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
ArchiveView: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class ExtensionBasedVersion(Version):
    __doc__: str
    extension: str
    def detect(self, extension: str, first_line: bytes) -> bool: ...

class HeaderBasedVersion(Version):
    __doc__: str
    header: bytes
    def detect(self, extension: str, first_line: bytes) -> bool: ...

class Version(metaclass=abc.ABCMeta):
    __doc__: str
    name: str
    def __str__(self) -> str: ...
    @abstractmethod
    def detect(self, extension: str, first_line: bytes) -> bool: ...
    @abstractmethod
    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]: ...
    def postprocess(self, source, sink: BinaryIO) -> None: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
