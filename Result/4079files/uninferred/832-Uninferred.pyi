import discord
from pcbot import utils as utils
from typing import Any

client: discord.Client
db: Any
command_pattern: Any
sessions: Any

async def options(arg: Any): ...
async def wouldyourather(message: discord.Message, opt: options=...) -> Any: ...
async def remove(message: discord.Message, opt: options) -> Any: ...
