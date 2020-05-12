from .store import SlackChannelItem, SlackStore
from typing import Any, Optional

logger: Any

class Group(SlackChannelItem):
    def __init__(self, id_: Any, raw: Optional[Any] = ..., last_update: Optional[Any] = ...) -> None: ...

class GroupStore(SlackStore):
    def __init__(self, client: Any, refresh: int = ...) -> None: ...
    async def all(self) -> None: ...
    async def get(self, id_: Optional[Any] = ..., fetch: bool = ...): ...
    async def _add(self, group: Any, db: Optional[Any] = ...) -> None: ...
    async def _delete(self, id_: Any, db: Optional[Any] = ...) -> None: ...
    async def _query(self, id_: Any): ...
