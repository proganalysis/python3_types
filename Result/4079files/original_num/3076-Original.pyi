# (generated with --quick)

from typing import Any, BinaryIO, FrozenSet, Optional, Tuple

ArchiveView: Any
HeaderBasedVersion: Any
MissingPackageError: Any
Version: Any
VersionSpecificRequirementUnmetError: Any
ast: module
io: module
itertools: module
loader_name: str
magic_keys: Tuple[int, int, int, int, int, int, int]
os: module
re: module
struct: module
versions: FrozenSet[type]

class IncorrectLoaderError(Any):
    def __init__(self) -> None: ...

class LoaderRequiredError(Any):
    __doc__: str
    def __init__(self, path: str) -> None: ...

class ZiX12A(Any):
    __doc__: str
    header: bytes
    name: str
    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]: ...

class ZiX12B(Any):
    __doc__: str
    details: Optional[Tuple[int, Any]]
    header: bytes
    name: str
    def __init__(self) -> None: ...
    def find_offset_and_key(self, archive: BinaryIO) -> Tuple[int, Optional[int]]: ...
    def postprocess(self, source, sink: BinaryIO) -> None: ...

def find_key(loader: str) -> int: ...
def find_offset(archive: BinaryIO) -> int: ...
def get_loader(archive: BinaryIO) -> str: ...
def obfuscation_offset(value: bytes) -> int: ...
def obfuscation_run(s: bytes, key: int) -> bytes: ...
def obfuscation_sha1(code: str) -> int: ...
