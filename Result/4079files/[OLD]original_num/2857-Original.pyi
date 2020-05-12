# (generated with --quick)

import __builtin__
import __future__
from typing import Any, Dict, List, Optional, Type, Union

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
    gfedb_version: str
    imgtdb_version: str
    log: List[str]
    message: str
    pygfe_version: str
    swagger_types: Dict[str, __builtin__.type[Union[str, List[str]]]]
    type: str
    def __init__(self, message: Optional[str] = ..., pygfe_version: Optional[str] = ..., gfedb_version: Optional[str] = ..., imgtdb_version: Optional[str] = ..., log: Optional[List[str]] = ..., type: Optional[str] = ...) -> None: ...
    @classmethod
    def from_dict(cls, dikt) -> Error: ...
