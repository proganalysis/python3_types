# (generated with --quick)

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
convert_custom_emoji: None
convert_disc_channel: None
convert_disc_mention: None
convert_irc_mention: None
convert_role_mention: None
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
    name: Any
    nick: Any
    port: Any
    realname: Any
    server_password: Any
    username: Any
    def __init__(self, name) -> None: ...
    def connect(self, **kwargs) -> Coroutine[Any, Any, None]: ...
    def get_discord_channel(self, irc) -> Any: ...
    def keepalive(self, message, **kwargs) -> None: ...
    def message(self, nick, target, message, **kwargs) -> Coroutine[Any, Any, None]: ...

class MDiscordTransform(Any):
    func: Any
    def __init__(self, name, module, func) -> None: ...
    def transform(self, message, author, discord_server, irc_client) -> coroutine: ...

class MIrcTransform(Any):
    func: Any
    def __init__(self, name, module, func) -> None: ...
    def transform(self, message, author, irc_client, discord_server) -> coroutine: ...

def discord_transform(name) -> Callable[[Any], Any]: ...
def irc_transform(name) -> Callable[[Any], Any]: ...
def load(loop) -> Coroutine[Any, Any, None]: ...
def prevent_ping(name) -> Any: ...
def unload(loop) -> Coroutine[Any, Any, None]: ...
