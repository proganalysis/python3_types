# (generated with --quick)

import asyncio.events
from typing import Any, Awaitable, Callable, Coroutine, List, Pattern, Set, Tuple

DiscordTransformType = Callable[[str, str, Any, Any], Awaitable[str]]
IrcTransformType = Callable[[str, Any, Any, Any], Awaitable[str]]

CHANNEL_RE: Pattern[str]
EMOJI_RE: Pattern[str]
IGNORED_NAMES: Set[str]
IRC_MENTION_RE: Pattern[str]
MChannel: Any
MENTION_RE: Pattern[str]
MHandler: Any
Message: Any
ROLE_RE: Pattern[str]
SnowflakeID: Any
User: Any
always_command: Any
asyncio: module
bottom: Any
convert_custom_emoji: Any
convert_disc_channel: Any
convert_disc_mention: Any
convert_irc_mention: Any
convert_role_mention: Any
ircrelay: Any
last_messages: list
logger: logging.Logger
logging: module
master: Any
messagelogger: logging.Logger
re: module

class IrcConnection:
    address: Any
    channels: List[Tuple[Any, Any]]
    client: Any
    name: str
    nick: Any
    port: Any
    realname: Any
    server_password: Any
    username: Any
    def __init__(self, name: str) -> None: ...
    def connect(self, **kwargs) -> Coroutine[Any, Any, None]: ...
    def get_discord_channel(self, irc: str) -> Any: ...
    def keepalive(self, message: str, **kwargs) -> None: ...
    def message(self, nick: str, target: str, message: str, **kwargs) -> Coroutine[Any, Any, None]: ...

class MDiscordTransform(Any):
    func: Callable[[str, str, Any, Any], Awaitable[str]]
    def __init__(self, name: str, module: str, func: Callable[[str, str, Any, Any], Awaitable[str]]) -> None: ...
    def transform(self, message: str, author: str, discord_server, irc_client) -> Coroutine[Any, Any, str]: ...

class MIrcTransform(Any):
    func: Callable[[str, Any, Any, Any], Awaitable[str]]
    def __init__(self, name: str, module: str, func: Callable[[str, Any, Any, Any], Awaitable[str]]) -> None: ...
    def transform(self, message: str, author, irc_client, discord_server) -> Coroutine[Any, Any, str]: ...

def discord_transform(name: str) -> Callable[[Callable[[str, str, Any, Any], Awaitable[str]]], None]: ...
def irc_transform(name: str) -> Callable[[Callable[[str, Any, Any, Any], Awaitable[str]]], None]: ...
def load(loop: asyncio.events.AbstractEventLoop) -> Coroutine[Any, Any, None]: ...
def prevent_ping(name: str) -> str: ...
def unload(loop: asyncio.events.AbstractEventLoop) -> Coroutine[Any, Any, None]: ...
