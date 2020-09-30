import typing
from enum import Enum as Enum
from typing import Any

EVERY_ENDPOINT_ARGS: Any
GET_COLLECTION_ARGS: Any
GET_SINGLETON_ARGS: Any
ALL_ARGS: Any

class NotStandardArg(Exception):
    def __init__(self, key: str) -> None: ...

def use_standard_args(*args: Any, locations: typing.Tuple[str, ...]=..., get_collection: bool=..., get_singleton: bool=..., webargs_schema: dict=...) -> Any: ...
