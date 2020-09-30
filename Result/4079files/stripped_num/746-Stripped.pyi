# (generated with --quick)

from typing import Any, Coroutine, Pattern

asyncio: module
checks: Any
commands: Any
dataIO: Any
discord: Any
os: module
re: module
send_cmd_help: Any
settings: module

class Antilink:
    __author__: str
    __doc__: str
    __version__: str
    add: Any
    antilinkset: Any
    bot: Any
    emoji_string: str
    exclude: Any
    json: Any
    location: str
    message: Any
    regex: Pattern[str]
    regex_discordme: Pattern[str]
    regex_url: Pattern[str]
    remove: Any
    toggle: Any
    toggledm: Any
    togglestrict: Any
    def __init__(self, bot) -> None: ...
    def _new_message(self, message) -> Coroutine[Any, Any, None]: ...

def check_file() -> None: ...
def check_folder() -> None: ...
def setup(bot) -> None: ...
