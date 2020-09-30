import logging
from typing import Any

logger: Any

def make_logger(name: Any, fname: Any=...) -> logging.Logger: ...
def exception_logger(func: Any): ...
