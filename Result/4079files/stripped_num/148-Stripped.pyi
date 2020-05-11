# (generated with --quick)

from typing import Any

logging: module

class LoggingConfig:
    _LoggingConfig__debug: Any
    _LoggingConfig__filename: Any
    _LoggingConfig__max_bytes: Any
    _LoggingConfig__root_logger: logging.Logger
    def __init__(self, filename, max_bytes) -> None: ...
    def enable_debug(self, debug) -> None: ...
    def get_logger(self) -> logging.Logger: ...
    def set_error_hadler(self, type, value, tb) -> None: ...
