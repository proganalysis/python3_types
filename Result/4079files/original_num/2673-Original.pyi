# (generated with --quick)

from typing import Iterable, Type, Union

StringOrStrings: Type[Union[str, Iterable[str]]]

class GutenbergException(Exception): ...

class InvalidUsage(GutenbergException):
    message: str
    status_code: int
    def __init__(self, message: str, status_code: int = ...) -> None: ...

class MisformedQuery(InvalidUsage):
    message: str
    status_code: int
    def __init__(self, query: str) -> None: ...

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
    def __init__(self, unknown: Union[str, Iterable[str]], known: Iterable[str]) -> None: ...

class UnknownQueryOperator(InvalidUsage):
    message: str
    status_code: int
    def __init__(self, unknown: str, known: Iterable[str]) -> None: ...
