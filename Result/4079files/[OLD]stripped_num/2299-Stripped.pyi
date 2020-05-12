# (generated with --quick)

from typing import Any, Coroutine, Set

Dogbot: Any
UTBR_MAXIMUM: int
WHITELISTED_GUILDS: Set[int]
discord: Any

def is_blacklisted(bot, guild_id) -> Coroutine[Any, Any, bool]: ...
def is_bot_collection(bot, guild) -> Coroutine[Any, Any, bool]: ...
def user_to_bot_ratio(guild) -> float: ...
