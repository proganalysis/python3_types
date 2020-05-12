from datetime import date as date, datetime as datetime
from swagger_server.models.base_model_ import Model
from typing import Any, List

class Error(Model):
    swagger_types: Any = ...
    attribute_map: Any = ...
    _message: Any = ...
    _pygfe_version: Any = ...
    _gfedb_version: Any = ...
    _imgtdb_version: Any = ...
    _log: Any = ...
    _type: Any = ...
    def __init__(self, message: str=..., pygfe_version: str=..., gfedb_version: str=..., imgtdb_version: str=..., log: List[str]=..., type: str=...) -> None: ...
    @classmethod
    def from_dict(cls: Any, dikt: Any) -> Error: ...
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, message: str) -> Any: ...
    @property
    def pygfe_version(self) -> str: ...
    @pygfe_version.setter
    def pygfe_version(self, pygfe_version: str) -> Any: ...
    @property
    def gfedb_version(self) -> str: ...
    @gfedb_version.setter
    def gfedb_version(self, gfedb_version: str) -> Any: ...
    @property
    def imgtdb_version(self) -> str: ...
    @imgtdb_version.setter
    def imgtdb_version(self, imgtdb_version: str) -> Any: ...
    @property
    def log(self) -> List[str]: ...
    @log.setter
    def log(self, log: List[str]) -> Any: ...
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, type: str) -> Any: ...
