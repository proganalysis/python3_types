# (generated with --quick)

from typing import TextIO

formatter: logging.Formatter
h1: logging.StreamHandler
h2: logging.StreamHandler
logger: logging.Logger
logging: module
stderr: TextIO
stdout: TextIO

class InfoFilter(logging.Filter):
    __doc__: str
    def filter(self, rec) -> bool: ...
