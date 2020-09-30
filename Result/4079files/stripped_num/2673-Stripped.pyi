# (generated with --quick)

from typing import Any, Iterable, Type, Union

StringOrStrings: Type[Union[str, Iterable[str]]]

class GutenbergException(Exception): ...

class InvalidUsage(GutenbergException):
    message: Any
    status_code: Any
    def __init__(self, message, status_code = ...) -> None: ...

class MisformedQuery(InvalidUsage):
    message: str
    status_code: int
    def __init__(self, query) -> None: ...

class NoQuery(InvalidUsage):
    message: str
    status_code: int
    def __init__(self) -> None: ...

class NoQueryValue(InvalidUsage):
    message: str
    status_code: int
    def __init__(self) -> None: ...

class UnknownFields(InvalidUsage):
    message: str
    status_code: int
    def __init__(self, unknown, known) -> None: ...

class UnknownQueryOperator(InvalidUsage):
    message: str
    status_code: int
    def __init__(self, unknown, known) -> None: ...
