from typing import Any, Iterable, Union

StringOrStrings = Union[Iterable[str], str]

class GutenbergException(Exception): ...

class InvalidUsage(GutenbergException):
    message: Any = ...
    status_code: Any = ...
    def __init__(self, message: str, status_code: int=...) -> None: ...

class UnknownFields(InvalidUsage):
    def __init__(self, unknown: StringOrStrings, known: Iterable[str]) -> None: ...

class NoQuery(InvalidUsage):
    def __init__(self) -> None: ...

class NoQueryValue(InvalidUsage):
    def __init__(self) -> None: ...

class MisformedQuery(InvalidUsage):
    def __init__(self, query: str) -> None: ...

class UnknownQueryOperator(InvalidUsage):
    def __init__(self, unknown: str, known: Iterable[str]) -> None: ...