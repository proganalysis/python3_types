# (generated with --quick)

import pathlib
from typing import Any, Dict, Type

DiffItem: Any
Path: Type[pathlib.Path]
json: module

class DiffHead(object):
    __doc__: str
    _base_version: Any
    _items: Any
    _protocol: Any
    _repository: Any
    _target_version: Any
    base_version: Any
    items: Any
    protocol: Any
    repository: Any
    target_version: Any
    def __init__(self, protocol, repository, base_version, target_version, items = ...) -> None: ...
    @staticmethod
    def load_dict(data) -> DiffHead: ...
    @staticmethod
    def load_json_file(filepath) -> DiffHead: ...
    def to_dict(self) -> Dict[str, Any]: ...
