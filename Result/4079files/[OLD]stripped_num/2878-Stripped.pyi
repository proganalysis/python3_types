# (generated with --quick)

from typing import Any, Coroutine, Dict

Context: Any
Embed: Any
Plugin: Any
UQRatio: Any
UWRatio: Any
attrdict: Any
command: Any
curio: Any
functools: module
group: Any
intersphinx: Any
logger: logging.Logger
logging: module
process: Any

class MockSphinxApp:
    __doc__: str
    config: Any
    logger: Any
    def __init__(self, logger) -> None: ...
    def info(self, msg) -> None: ...
    def warn(self, msg) -> None: ...

class Pydoc(Any):
    __doc__: str
    _app: MockSphinxApp
    _item_lengths: Dict[Any, int]
    invdata: Dict[Any, dict]
    pydoc: Any
    sources: Any
    def __init__(self, bot) -> None: ...
    def _setup_pydocs(self) -> Coroutine[Any, Any, None]: ...
    def load(self) -> Coroutine[Any, Any, None]: ...
