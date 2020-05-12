from .common import Cog
from typing import Any

JOSE_SERVER: int
ROLE_ID: int

class Subscribe(Cog):
    def __init__(self, bot: Any) -> None: ...
    def __local_check(self, ctx: Any): ...
    def get_role(self, ctx: Any, roleid: Any): ...
    async def sub(self, ctx: Any) -> None: ...
    async def unsub(self, ctx: Any) -> None: ...
    async def callout(self, ctx: Any, msg: str) -> Any: ...

def setup(bot: Any) -> None: ...
