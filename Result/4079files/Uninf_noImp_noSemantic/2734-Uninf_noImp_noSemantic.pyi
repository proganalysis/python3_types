from abc import ABCMeta, abstractmethod
from typing import BinaryIO, Optional, Tuple
from unrpa.view import ArchiveView

class Version(metaclass=ABCMeta):
    name: str
    @abstractmethod
    def detect(self, extension: str, first_line: bytes) -> bool: ...
    @abstractmethod
    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]: ...
    def postprocess(self, source: ArchiveView, sink: BinaryIO) -> None: ...
    def __str__(self) -> str: ...

class ExtensionBasedVersion(Version, metaclass=ABCMeta):
    extension: str
    def detect(self, extension: str, first_line: bytes) -> bool: ...

class HeaderBasedVersion(Version, metaclass=ABCMeta):
    header: bytes
    def detect(self, extension: str, first_line: bytes) -> bool: ...
