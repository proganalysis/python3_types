import asyncio
from typing import Any

bot: Any

def is_me(m: Any): ...
def is_num(s: Any): ...
def roll_basic(a: Any, b: Any, modifier: Any, threshold: Any): ...
def roll_hit(num_of_dice: Any, dice_type: Any, hit: Any, modifier: Any, threshold: Any): ...
@asyncio.coroutine
def on_ready() -> None: ...
@asyncio.coroutine
def roll(ctx: Any, roll: str) -> Any: ...
@asyncio.coroutine
def purge(ctx: Any) -> None: ...
