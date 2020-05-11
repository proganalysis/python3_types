# (generated with --quick)

import configparser
import pathlib
from typing import Any, Optional, Pattern, Tuple, Type

Formatter: Type[logging.Formatter]
LOG: logging.Logger
NAPP_ID_RE: Pattern[str]
Path: Type[pathlib.Path]
RawConfigParser: Type[configparser.RawConfigParser]
WebSocketHandler: Any
__all__: Tuple[str, str]
config: module
inspect: module
logging: module
re: module
root_handler: logging.Handler

class LogManager:
    _DEFAULT_FMT: str
    _PARSER: configparser.RawConfigParser
    __doc__: str
    @classmethod
    def _catch_config_file_exception(cls, config_file) -> None: ...
    @classmethod
    def _set_debug_mode(cls, debug = ...) -> None: ...
    @classmethod
    def _use_config_file(cls, config_file) -> None: ...
    @classmethod
    def add_handler(cls, handler) -> None: ...
    @classmethod
    def enable_websocket(cls, socket) -> Any: ...
    @staticmethod
    def filter_session_disconnected(record) -> bool: ...
    @classmethod
    def load_config_file(cls, config_file, debug = ...) -> None: ...

class NAppLog:
    __doc__: str
    def __getattribute__(self, name) -> Any: ...

def HANDLER_FILTER(record) -> bool: ...
def _detect_napp_id() -> Optional[str]: ...
def getLogger(name: Optional[str] = ...) -> logging.Logger: ...
