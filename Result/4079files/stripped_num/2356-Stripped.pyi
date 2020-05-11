# (generated with --quick)

import collections
from typing import Any, Coroutine, Type

Weeabot: Any
checks: Any
commands: Any
defaultdict: Type[collections.defaultdict]
discord: Any
request: Any

class Roles:
    bot: Any
    hide: Any
    make_channel: Any
    makeme: Any
    roles: Any
    unhide: Any
    def __init__(self, bot) -> None: ...
    def check_config(self, ctx) -> Coroutine[Any, Any, None]: ...
    def get_roles_list(self, ctx) -> Coroutine[Any, Any, collections.defaultdict]: ...
    def update_roles(self, ctx) -> Coroutine[Any, Any, None]: ...

def setup(bot) -> None: ...
