# (generated with --quick)

from typing import Any, Coroutine

SlackChannelItem: Any
SlackStore: Any
database: Any
json: module
logger: logging.Logger
logging: module
registry: Any
time: module

class Group(Any):
    __doc__: str
    def __init__(self, id_, raw = ..., last_update = ...) -> None: ...

class GroupStore(Any):
    __doc__: str
    def __init__(self, client, refresh = ...) -> None: ...
    def _add(self, group, db = ...) -> Coroutine[Any, Any, None]: ...
    def _delete(self, id_, db = ...) -> Coroutine[Any, Any, None]: ...
    def _query(self, id_) -> Coroutine[Any, Any, Group]: ...
    def all(self) -> Coroutine[Any, Any, None]: ...
    def get(self, id_ = ..., fetch = ...) -> Coroutine[Any, Any, Group]: ...
