# (generated with --quick)

from typing import Any, Coroutine, Dict, Optional, Union

asyncio: module
checks: Any
commands: Any
dataIO: Any
default_settings: Dict[str, Optional[Union[bool, str]]]
discord: Any
os: module
send_cmd_help: module

class Bouncer:
    __doc__: str
    bot: Any
    bouncerset: Any
    bouncerset_kickmessage: Any
    bouncerset_logchannel: Any
    bouncerset_mode: Any
    bouncerset_roles: Any
    bouncerset_rules: Any
    bouncerset_timeoutmessage: Any
    bouncerset_toggle: Any
    bouncerset_welcomemessage: Any
    settings: Any
    def __init__(self, bot) -> None: ...
    def bounce(self, target, message, user) -> Coroutine[Any, Any, Optional[bool]]: ...
    def on_member_join(self, member) -> Coroutine[Any, Any, None]: ...
    def writelog(self, server, message) -> Coroutine[Any, Any, None]: ...

def check_files() -> None: ...
def check_folders() -> None: ...
def setup(bot) -> None: ...
