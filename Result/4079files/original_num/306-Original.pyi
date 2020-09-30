# (generated with --quick)

import pathlib
from typing import Any, Type

Path: Type[pathlib.Path]
abc: module
json: module
logger: logging.Logger
logging: module
networkx: module

class BaseRepository(abc.ABC):
    _absolute_path: pathlib.Path
    _metadata: Any
    absolute_path: Any
    first_version: str
    info_path: pathlib.Path
    latest_version: str
    name: str
    protocol: int
    strategy: str
    version_graph: Any
    version_graph_path: pathlib.Path
    def __init__(self, absolute_path: pathlib.Path) -> None: ...
    def has_version(self, name: str) -> Any: ...

class ProtocolException(Exception): ...
