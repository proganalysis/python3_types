# (generated with --quick)

from typing import Any, List

ARGS_DESC: dict
ARGS_HEADER: dict
ARGS_LABEL: dict
ARGS_OPTIONS: dict
ARGS_SCRIPT: dict
ARGS_VERSION: dict
C: Any
SCRIPT: Any
__all__: List[str]
_old_docopt: Any
docopt_file: Any
docopt_version: Any
sys: module

class _ColorDocoptExit(SystemExit):
    __doc__: str
    usage: str
    def __init__(self, message = ...) -> None: ...

def _coloredhelp(s) -> str: ...
def _docoptextras(help, version, options, doc) -> None: ...
def docopt(doc, argv = ..., help = ..., version = ..., options_first = ..., script = ..., colors = ...) -> Any: ...
