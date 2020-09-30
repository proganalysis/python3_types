# (generated with --quick)

from typing import Any

Cog: Any
JOSE_SERVER: int
ROLE_ID: int
commands: Any

class Subscribe(Any):
    __doc__: str
    callout: Any
    sub: Any
    unsub: Any
    def _Subscribe__local_check(self, ctx) -> Any: ...
    def __init__(self, bot) -> None: ...
    def get_role(self, ctx, roleid) -> Any: ...

def setup(bot) -> None: ...
