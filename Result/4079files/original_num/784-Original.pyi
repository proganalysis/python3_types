# (generated with --quick)

from typing import Any, Callable, Coroutine

CHECKSETTING_TEMPLATE: str
aioredis: Any
command: Any
core: Any
guild_only: Any
has_permissions: Any
os: module
re: module

class ProblemReporter:
    ctx: Any
    problems: list
    def __aenter__(self) -> Coroutine[Any, Any, Callable[[Any], Any]]: ...
    def __aexit__(self, type, value, traceback) -> Coroutine[Any, Any, None]: ...
    def __init__(self, ctx) -> None: ...
    def _report(self, text) -> None: ...

class SettingsModule:
    _set: Any
    checkallsettings: Any
    checkdmsettings: Any
    checksetting: Any
    expand_value: Callable
    prefix: Any
    reduce_value: Callable
    setprefix: Any
    theme: Any
    units: Any

class WasProblems(Exception): ...

def setup(bot) -> None: ...
