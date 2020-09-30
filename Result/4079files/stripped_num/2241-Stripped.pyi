# (generated with --quick)

import __future__
from typing import Any, Dict, Type, Union

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
    accession: Any
    attribute_map: Dict[str, str]
    rank: Any
    sequence: Any
    swagger_types: Dict[str, Type[Union[int, str]]]
    term: Any
    def __init__(self, accession = ..., rank = ..., sequence = ..., term = ...) -> None: ...
    @classmethod
    def from_dict(cls, dikt) -> Any: ...
