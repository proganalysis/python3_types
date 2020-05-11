# (generated with --quick)

from typing import Any, Tuple

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
    def __call__(self, client, datatype, datavalue) -> Any: ...
    def commonsMedia__string(self, client, datavalue) -> Any: ...
    def monolingualtext(self, client, datavalue) -> Any: ...
    def string(self, client, datavalue) -> Any: ...
    def time(self, client, datavalue) -> datetime.date: ...
    def wikibase_entityid(self, client, datavalue) -> Any: ...
