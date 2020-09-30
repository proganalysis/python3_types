# (generated with --quick)

from typing import Any, Coroutine

asyncio: module
checks: Any
commands: Any
dataIO: Any
discord: Any
os: module
send_cmd_help: module

class NameChange:
    __doc__: str
    bot: Any
    cooldown: dict
    namechangeset: Any
    namechangeset_channel: Any
    namechangeset_cooldown: Any
    namechangeset_toggle: Any
    settings: Any
    def __init__(self, bot) -> None: ...
    def on_member_update(self, before, after) -> Coroutine[Any, Any, None]: ...
    def purger_task(self, member) -> Coroutine[Any, Any, None]: ...

def check_files() -> None: ...
def check_folders() -> None: ...
def setup(bot) -> None: ...
