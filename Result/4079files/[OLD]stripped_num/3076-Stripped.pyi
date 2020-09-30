# (generated with --quick)

from typing import Any, FrozenSet, Optional, Tuple, Type, Union

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
versions: FrozenSet[Type[Union[ZiX12A, ZiX12B]]]

class IncorrectLoaderError(Any):
    def __init__(self) -> None: ...

class LoaderRequiredError(Any):
    __doc__: str
    def __init__(self, path) -> None: ...

class ZiX12A(Any):
    __doc__: str
    header: bytes
    name: str
    def find_offset_and_key(self, archive) -> Tuple[Any, Any]: ...

class ZiX12B(Any):
    __doc__: str
    details: Optional[Tuple[Any, Any]]
    header: bytes
    name: str
    def __init__(self) -> None: ...
    def find_offset_and_key(self, archive) -> Tuple[Any, Any]: ...
    def postprocess(self, source, sink) -> None: ...

def find_key(loader) -> int: ...
def find_offset(archive) -> int: ...
def get_loader(archive) -> str: ...
def obfuscation_offset(value) -> int: ...
def obfuscation_run(s, key) -> bytes: ...
def obfuscation_sha1(code) -> int: ...
