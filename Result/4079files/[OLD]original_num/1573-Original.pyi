# (generated with --quick)

from typing import Optional, Set, Type
import unrpa.versions.version

Version: Type[unrpa.versions.version.Version]

class AmbiguousArchiveError(UnRPAError):
    __doc__: str
    cmd_line_help: Optional[str]
    message: str
    versions: Set[unrpa.versions.version.Version]
    def __init__(self, detected: Set[unrpa.versions.version.Version]) -> None: ...

class ErrorExtractingFile(UnRPAError):
    __doc__: str
    cmd_line_help: Optional[str]
    message: str
    def __init__(self, detail: str) -> None: ...

class OutputDirectoryNotFoundError(UnRPAError):
    __doc__: str
    cmd_line_help: Optional[str]
    message: str
    def __init__(self, path: str) -> None: ...

class UnRPAError(Exception):
    __doc__: str
    cmd_line_help: Optional[str]
    message: str
    def __init__(self, message: str, cmd_line_help: Optional[str] = ...) -> None: ...

class UnknownArchiveError(UnRPAError):
    __doc__: str
    cmd_line_help: Optional[str]
    header: bytes
    message: str
    def __init__(self, header: bytes) -> None: ...
