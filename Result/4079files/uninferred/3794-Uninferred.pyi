from discord.ext.commands import Context as Context
from typing import Any

def command_error_handler(exception: Exception) -> Any: ...
def format_command_error(ex: Exception, context: Context) -> tuple: ...
def format_traceback(tb: str) -> Any: ...