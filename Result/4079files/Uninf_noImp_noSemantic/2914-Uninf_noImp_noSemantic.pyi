from curious.commands.context import Context
from curious.commands.plugin import Plugin
from typing import Any

class Moderation(Plugin):
    async def cleanup(self, ctx: Context) -> Any: ...
    async def xban(self, ctx: Context, user_id: int) -> Any: ...
