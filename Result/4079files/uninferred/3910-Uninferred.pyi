import docopt as docopt
from typing import Any

docopt_version: Any
docopt_file: Any

class _ColorDocoptExit(SystemExit):
    usage: str = ...
    def __init__(self, message: str = ...) -> None: ...
