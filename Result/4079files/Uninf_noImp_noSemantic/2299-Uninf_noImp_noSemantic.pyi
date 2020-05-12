import discord
from dog import Dogbot
from typing import Any

WHITELISTED_GUILDS: Any
UTBR_MAXIMUM: int

def user_to_bot_ratio(guild: discord.Guild) -> Any: ...
async def is_blacklisted(bot: Dogbot, guild_id: int) -> bool: ...
async def is_bot_collection(bot: Dogbot, guild: discord.Guild) -> bool: ...
