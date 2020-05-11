# (generated with --quick)

import enum
from typing import Any, Dict, Optional, Tuple, Type

ALL_ARGS: Dict[str, Any]
Bool: Any
Date: Any
DelimitedList: Any
EVERY_ENDPOINT_ARGS: Dict[str, Any]
Enum: Type[enum.Enum]
GET_COLLECTION_ARGS: Dict[str, Any]
GET_SINGLETON_ARGS: Dict[str, Any]
Int: Any
Str: Any
typing: module
use_args: Any

class NotStandardArg(Exception):
    __doc__: str
    def __init__(self, key: str) -> None: ...

def use_standard_args(*args, locations: Tuple[str, ...] = ..., get_collection: bool = ..., get_singleton: bool = ..., webargs_schema: Optional[dict] = ...) -> Any: ...
