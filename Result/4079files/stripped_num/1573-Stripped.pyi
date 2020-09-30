# (generated with --quick)

from typing import Any, Type
import unrpa.versions.version

Version: Type[unrpa.versions.version.Version]

class AmbiguousArchiveError(UnRPAError):
    __doc__: str
    cmd_line_help: str
    message: str
    versions: Any
    def __init__(self, detected) -> None: ...

class ErrorExtractingFile(UnRPAError):
    __doc__: str
    cmd_line_help: str
    message: str
    def __init__(self, detail) -> None: ...

class OutputDirectoryNotFoundError(UnRPAError):
    __doc__: str
    cmd_line_help: str
    message: str
    def __init__(self, path) -> None: ...

class UnRPAError(Exception):
    __doc__: str
    cmd_line_help: Any
    message: Any
    def __init__(self, message, cmd_line_help = ...) -> None: ...

class UnknownArchiveError(UnRPAError):
    __doc__: str
    cmd_line_help: str
    header: Any
    message: str
    def __init__(self, header) -> None: ...
