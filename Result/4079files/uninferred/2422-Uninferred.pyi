from typing import Any

mal_config: Any
anilist_config: Any

async def postgres() -> None: ...
async def sqlite() -> None: ...
