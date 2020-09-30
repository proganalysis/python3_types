# (generated with --quick)

import __future__
from typing import Any, Dict, Optional, Type, Union

Model: Any
absolute_import: __future__._Feature
date: Type[datetime.date]
datetime: Type[datetime.datetime]
util: Any

class Feature(Any):
    __doc__: str
    _accession: Any
    _rank: Any
    _sequence: Any
    _term: Any
    accession: int
    attribute_map: Dict[str, str]
    rank: int
    sequence: str
    swagger_types: Dict[str, Type[Union[int, str]]]
    term: str
    def __init__(self, accession: Optional[int] = ..., rank: Optional[int] = ..., sequence: Optional[str] = ..., term: Optional[str] = ...) -> None: ...
    @classmethod
    def from_dict(cls, dikt) -> Feature: ...
