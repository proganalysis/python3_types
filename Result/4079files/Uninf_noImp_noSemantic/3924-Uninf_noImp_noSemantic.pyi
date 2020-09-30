from discord.ext import commands
from typing import Any

class GuildConverter(commands.IDConverter):
    async def convert(self, ctx: commands.Context, argument: str) -> Any: ...

class UserInfoConverter(commands.IDConverter):
    async def convert(self, ctx: commands.Context, argument: str) -> Any: ...

class UnspecifiedConverter(commands.IDConverter):
    async def convert(self, ctx: commands.Context, argument: str) -> Any: ...
