from ika.service import Command
from typing import Any

class Stop(Command):
    name: str = ...
    aliases: Any = ...
    syntax: str = ...
    regex: str = ...
    permission: Any = ...
    description: Any = ...
    async def execute(self, user: Any, reason: Any) -> None: ...
