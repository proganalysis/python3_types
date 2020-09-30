# (generated with --quick)

import typing
from typing import Any, NoReturn

InvalidConfiguration: Any

class AbstractCast(object):
    def __call__(self, value) -> NoReturn: ...

class Boolean(AbstractCast):
    default_values: dict
    values: dict
    def __call__(self, value) -> Any: ...
    def __init__(self, values = ...) -> None: ...

class List(AbstractCast):
    delimiter: Any
    quotes: Any
    def __call__(self, value) -> Any: ...
    def __init__(self, delimiter = ..., quotes = ...) -> None: ...
    def _parse(self, string) -> typing.List[str]: ...
    def cast(self, sequence) -> list: ...

class Option(AbstractCast):
    __doc__: str
    options: Any
    def __call__(self, value) -> Any: ...
    def __init__(self, options) -> None: ...

class Tuple(List):
    delimiter: Any
    quotes: Any
    def cast(self, sequence) -> tuple: ...
