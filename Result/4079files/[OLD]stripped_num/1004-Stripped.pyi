# (generated with --quick)

from typing import Any, Callable, Dict, Union

Blueprint: Any
QUOTES_PRIVATE: Dict[str, Union[bool, str]]
functools: module
g: Any
guild_all: Any
guild_quote: Any
guild_resolver: Any
json: Any
quotes: Any

def get_quotes(guild) -> Any: ...
def guild_exposes_quotes(guild) -> Any: ...
def quotes_resolver(func) -> Callable: ...
