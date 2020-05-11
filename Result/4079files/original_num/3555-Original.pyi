# (generated with --quick)

import pathlib
from typing import Any, Dict, Optional, Type

DiffItem: Any
Path: Type[pathlib.Path]
json: module

class DiffHead(object):
    __doc__: str
    _base_version: str
    _items: Any
    _protocol: int
    _repository: str
    _target_version: str
    base_version: str
    items: list
    protocol: int
    repository: str
    target_version: str
    def __init__(self, protocol: int, repository: str, base_version: str, target_version: str, items: Optional[list] = ...) -> None: ...
    @staticmethod
    def load_dict(data: Dict[str, Any]) -> DiffHead: ...
    @staticmethod
    def load_json_file(filepath: pathlib.Path) -> DiffHead: ...
    def to_dict(self) -> Dict[str, Any]: ...
