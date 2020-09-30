# (generated with --quick)

from typing import Any

gdb: Any

class ArgumentTypeError(InvalidArgumentError):
    __doc__: str
    _fmt: str
    val: Any
    def __init__(self, name, val, expected_type) -> None: ...
    def format_clsname(self, cls) -> Any: ...

class CorruptedError(RuntimeError):
    __doc__: str

class DelayedAttributeError(AttributeError):
    __doc__: str
    name: Any
    def __init__(self, name) -> None: ...

class IncompatibleGDBError(RuntimeError):
    __doc__: str
    _fmt: str
    def __init__(self, message) -> None: ...

class InvalidArgumentError(TypeError):
    __doc__: str

class MissingSymbolError(RuntimeError):
    __doc__: str

class MissingTypeError(RuntimeError):
    __doc__: str

class NotStructOrUnionError(UnexpectedGDBTypeBaseError):
    __doc__: str
    _fmt: str
    def __init__(self, name, gdbtype) -> None: ...

class UnexpectedGDBTypeBaseError(InvalidArgumentError):
    __doc__: str

class UnexpectedGDBTypeError(UnexpectedGDBTypeBaseError):
    __doc__: str
    _fmt: str
    def __init__(self, name, val, expected_type) -> None: ...
