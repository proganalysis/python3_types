# (generated with --quick)

import srctools.bsp_transform
import srctools.logger
from typing import Any, Callable, Type

Context: Type[srctools.bsp_transform.Context]
Entity: Any
LOGGER: srctools.logger.LoggerAdapter
RELAY_MAX: int
proxy_limits: Any

def get_logger(name = ..., alias = ...) -> srctools.logger.LoggerAdapter: ...
def trans(name) -> Callable[[Any], Any]: ...
