import discord
from typing import Any

class NameChange:
    bot: Any = ...
    cooldown: Any = ...
    settings: Any = ...
    def __init__(self, bot: Any) -> None: ...
    async def namechangeset(self, ctx: Any) -> None: ...
    async def namechangeset_toggle(self, ctx: Any, on_off: bool) -> Any: ...
    async def namechangeset_channel(self, ctx: Any, channel: discord.Channel) -> Any: ...
    async def namechangeset_cooldown(self, ctx: Any, seconds: int) -> Any: ...
    async def on_member_update(self, before: Any, after: Any) -> None: ...
    async def purger_task(self, member: Any) -> None: ...

def check_folders() -> None: ...
def check_files() -> None: ...
def setup(bot: Any) -> None: ...