# (generated with --quick)

import __builtin__
import __future__
from typing import Any, Dict, List, Type, Union

Model: Any
absolute_import: __future__._Feature
date: Type[datetime.date]
datetime: Type[datetime.datetime]
util: Any

class Error(Any):
    __doc__: str
    _gfedb_version: Any
    _imgtdb_version: Any
    _log: Any
    _message: Any
    _pygfe_version: Any
    _type: Any
    attribute_map: Dict[str, str]
    gfedb_version: Any
    imgtdb_version: Any
    log: Any
    message: Any
    pygfe_version: Any
    swagger_types: Dict[str, __builtin__.type[Union[str, List[str]]]]
    type: Any
    def __init__(self, message = ..., pygfe_version = ..., gfedb_version = ..., imgtdb_version = ..., log = ..., type = ...) -> None: ...
    @classmethod
    def from_dict(cls, dikt) -> Any: ...
