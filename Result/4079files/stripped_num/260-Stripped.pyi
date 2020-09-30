# (generated with --quick)

from typing import Any, Coroutine, Tuple

ChangeName: Any
Command: Any
Nickname: Any
Permission: Any

class Ungroup(Any):
    aliases: Tuple[str, str, str]
    description: Tuple[str, str, str, str]
    name: str
    permission: Any
    regex: str
    syntax: str
    def execute(self, user, name) -> Coroutine[Any, Any, None]: ...
