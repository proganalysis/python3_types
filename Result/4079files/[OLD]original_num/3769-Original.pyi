# (generated with --quick)

from typing import Any, Mapping, Tuple

Client: Any
Entity: Any
File: Any
MonolingualText: Any
__all__: Tuple[str, str]
collections: module
datetime: module

class DatavalueError(ValueError):
    __doc__: str
    datavalue: Any
    def __init__(self, *args) -> None: ...

class Decoder:
    __doc__: str
    def __call__(self, client, datatype: str, datavalue: Mapping[str, object]) -> Any: ...
    def commonsMedia__string(self, client, datavalue: Mapping[str, object]) -> Any: ...
    def monolingualtext(self, client, datavalue: Mapping[str, object]) -> Any: ...
    def string(self, client, datavalue: Mapping[str, object]) -> str: ...
    def time(self, client, datavalue: Mapping[str, object]) -> datetime.date: ...
    def wikibase_entityid(self, client, datavalue: Mapping[str, object]) -> Any: ...
