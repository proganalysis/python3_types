import colorlog
from typing import Any, Optional

class SafeColoredFormatter(colorlog.ColoredFormatter):
    def format(self, record: Any): ...
ColoredFormatter = SafeColoredFormatter

def setup_logging(loglevel: Any, logfile: Optional[Any] = ...) -> None: ...
