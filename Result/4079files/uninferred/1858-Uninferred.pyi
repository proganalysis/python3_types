from enum import Enum
from logging.handlers import RotatingFileHandler as RotatingFileHandler
from typing import Any, Optional

log: Any

class OutputType(Enum):
    PLAIN: int = ...
    DEV: int = ...
    JSON: int = ...

g_file_handler: Any
g_stream_handler: Any

def setup_logging(outputtype: Any = ..., debug: bool = ..., unbuffered: bool = ..., logfile: Optional[Any] = ..., dev_allow_colors: bool = ..., dev_split: bool = ..., dev_module_verbose: bool = ..., dev_force_fmt: Optional[Any] = ..., dev_force_no_tty: Optional[Any] = ..., custom_log_levels: Optional[Any] = ...): ...
