from bot.error_handler import command_error_handler as command_error_handler, format_command_error as format_command_error, format_traceback as format_traceback
from bot.logger import command_formatter as command_formatter
from bot.session_manager import SessionManager as SessionManager
from core import argument_parser as argument_parser
from data_controller.mongo import MongoClient
from discord.ext.commands import Bot
from typing import Any

class HahaNoUR(Bot):
    prefix: Any = ...
    colour: Any = ...
    start_time: Any = ...
    logger: Any = ...
    help_general: Any = ...
    all_help: Any = ...
    db: Any = ...
    idol_names: Any = ...
    session_manager: Any = ...
    error_log: Any = ...
    feedbag_log: Any = ...
    def __init__(self, prefix: str, start_time: int, colour: int, logger: Any, session_manager: SessionManager, db: MongoClient, error_log: int, feedback_log: int, shard_id: int, shard_count: int) -> None: ...
    def start_bot(self, cogs: list, token: str) -> Any: ...
    async def __change_presence(self) -> None: ...
    async def send_traceback(self, tb: Any, header: Any) -> None: ...
    async def on_ready(self) -> None: ...
    async def process_commands(self, message: Any) -> None: ...
    async def on_error(self, event_method: Any, *args: Any, **kwargs: Any) -> None: ...
    async def __try_send_msg(self, channel: Any, author: Any, msg: Any) -> None: ...
    async def on_command_error(self, exception: Any, context: Any) -> None: ...
