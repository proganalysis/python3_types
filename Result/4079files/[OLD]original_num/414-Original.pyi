# (generated with --quick)

import logging
import srctools.bsp_transform
from typing import Any, Callable, Optional, Type

Context: Type[srctools.bsp_transform.Context]
Entity: Any
LOGGER: logging.Logger
RELAY_MAX: int
proxy_limits: Callable[[srctools.bsp_transform.Context], None]

def get_logger(name: str = ..., alias: Optional[str] = ...) -> logging.Logger: ...
def trans(name: str) -> Callable[[Callable[[srctools.bsp_transform.Context], None]], Callable[[srctools.bsp_transform.Context], None]]: ...
