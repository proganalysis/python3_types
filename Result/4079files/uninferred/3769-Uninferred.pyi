import datetime
from .client import Client
from .commonsmedia import File
from .entity import Entity
from .multilingual import MonolingualText
from typing import Any, Mapping, Union

class DatavalueError(ValueError):
    def __init__(self, *args: Any) -> None: ...
    @property
    def datavalue(self): ...
    def __str__(self) -> str: ...

class Decoder:
    def __call__(self, client: Client, datatype: str, datavalue: Mapping[str, object]) -> object: ...
    def wikibase_entityid(self, client: Client, datavalue: Mapping[str, object]) -> Entity: ...
    def string(self, client: Client, datavalue: Mapping[str, object]) -> str: ...
    def time(self, client: Client, datavalue: Mapping[str, object]) -> Union[datetime.date, datetime.datetime]: ...
    def monolingualtext(self, client: Client, datavalue: Mapping[str, object]) -> MonolingualText: ...
    def commonsMedia__string(self, client: Client, datavalue: Mapping[str, object]) -> File: ...