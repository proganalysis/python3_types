# (generated with --quick)

import _importlib_modulespec
import logging
from typing import Any, Dict, Tuple, Union

EXCEPTION_MESSAGE: Any
additionalModulePath: bool
bl_info: Dict[str, Union[str, Tuple[int, ...]]]
core: module
core_logger: logging.Logger
e: Exception
export: Any
interface: Any
operators: Any
os: module
properties: Any
sys: module

def log_callstack(back_trace = ...) -> Any: ...
def register() -> None: ...
def reload(module: _importlib_modulespec.ModuleType) -> _importlib_modulespec.ModuleType: ...
def unregister() -> None: ...
