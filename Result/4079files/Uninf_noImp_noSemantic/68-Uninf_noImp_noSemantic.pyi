from discord.ext import commands
from typing import Any

log: Any
bot: Any

async def on_ready() -> None: ...
async def on_command_error(ctx: commands.Context, e: Exception) -> Any: ...
