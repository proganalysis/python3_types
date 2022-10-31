from typing import Any, BinaryIO, FrozenSet, Optional, Tuple, Type
from unrpa.versions.errors import VersionSpecificRequirementUnmetError
from unrpa.versions.version import HeaderBasedVersion, Version as Version
from unrpa.view import ArchiveView

loader_name: str

def get_loader(archive: BinaryIO) -> str: ...
def find_key(loader: str) -> int: ...
def find_offset(archive: BinaryIO) -> int: ...

class ZiX12A(HeaderBasedVersion):
    name: str = ...
    header: bytes = ...
    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]: ...

class ZiX12B(HeaderBasedVersion):
    name: str = ...
    header: bytes = ...
    details: Any = ...
    def __init__(self) -> None: ...
    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]: ...
    def postprocess(self, source: ArchiveView, sink: BinaryIO) -> None: ...

versions: FrozenSet[Type[Version]]

class LoaderRequiredError(VersionSpecificRequirementUnmetError):
    def __init__(self, path: str) -> None: ...

class IncorrectLoaderError(VersionSpecificRequirementUnmetError):
    def __init__(self) -> None: ...

magic_keys: Any

def obfuscation_sha1(code: str) -> int: ...
def obfuscation_offset(value: bytes) -> int: ...
def obfuscation_run(s: bytes, key: int) -> bytes: ...