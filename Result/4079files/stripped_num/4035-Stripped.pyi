# (generated with --quick)

from typing import Any, Coroutine, Tuple

Command: Any
Permission: Any

class Stop(Any):
    aliases: Tuple[nothing, ...]
    description: Tuple[str, str, str]
    name: str
    permission: Any
    regex: str
    syntax: str
    def execute(self, user, reason) -> Coroutine[Any, Any, None]: ...
