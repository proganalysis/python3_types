# (generated with --quick)

import collections
import itertools
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

ZNODE_ACL: List[Dict[str, Union[int, str]]]
chain: Type[itertools.chain]
datetime: module
defaultdict: Type[collections.defaultdict]
jafka: module
json: module
kazoo: Any
os: module
sys: module
threading: module
zk: _zk

_T0 = TypeVar('_T0')
_T_zk = TypeVar('_T_zk', bound=_zk)

class Record:
    backlog: Any
    broker_id: Any
    consumer_id: Any
    consumer_offset: Any
    lastmtime: Any
    partition_id: Any
    topic: Any
    total_offset: Any
    def __init__(self, topic = ..., broker_id = ..., partition_id = ..., consumer_offset = ..., total_offset = ..., backlog = ..., consumer_id = ..., lastmtime = ...) -> None: ...
    def data(self, group: _T0) -> Tuple[_T0, Any, Any, Any, Any, Any, Any, Any]: ...

class _zk:
    client: Any
    hosts: Any
    started: bool
    def __enter__(self: _T_zk) -> _T_zk: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, hosts = ..., **kwargs) -> None: ...
    def create(self, path, data) -> Any: ...
    def delete(self, path) -> Any: ...
    def ensure(self, path) -> Any: ...
    def get(self, path) -> Any: ...
    def gets(self, path) -> Tuple[Any, Any]: ...
    def list(self, path) -> Any: ...
    def rdelete(self, path) -> Any: ...
    def set(self, path, data) -> Any: ...
    def start(self) -> None: ...

def main(zk) -> None: ...
