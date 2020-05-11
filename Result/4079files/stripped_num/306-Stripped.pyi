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
    _absolute_path: Any
    _metadata: Any
    absolute_path: Any
    first_version: Any
    info_path: Any
    latest_version: Any
    name: Any
    protocol: Any
    strategy: Any
    version_graph: Any
    version_graph_path: Any
    def __init__(self, absolute_path) -> None: ...
    def has_version(self, name) -> Any: ...

class ProtocolException(Exception): ...
