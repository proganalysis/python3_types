from curious.commands.context import Context as Context
from curious.commands.plugin import Plugin
from typing import Any

AUTHORIZATION_URL: str

def has_admin(ctx: Context) -> Any: ...

class Fuyu(Plugin):
    async def plugin_check(self, ctx: Context) -> Any: ...
    async def servername(self, ctx: Context, server_name: str) -> Any: ...
