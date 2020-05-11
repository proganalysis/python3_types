# (generated with --quick)

from typing import Any, Dict

ANSI_BOLD: Any
ANSI_COLOR: Any
ANSI_RESET: Any
CGAColors: Any
DEFAULT_FORMAT: str
LEVEL_COLORS: Dict[int, Any]
logging: module

class ColorFormatter(ComposableFormatter):
    _parent_formatter: Any
    _use_color: Any
    def format(self, *args, **kwargs) -> Any: ...
    def new_formatter(self, fmt, *args, **kwargs) -> logging.Formatter: ...
    def reformat(self, fmt) -> Any: ...
    @staticmethod
    def remove_color(fmt) -> Any: ...

class ComposableFormatter(object):
    _parent_formatter: Any
    def __getattr__(self, name) -> Any: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def new_formatter(self, *args, **kwargs) -> logging.Formatter: ...
