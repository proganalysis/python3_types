from typing import Any

docopt_version: Any
docopt_file: Any
__all__: Any
SCRIPT: Any
ARGS_DESC: Any
ARGS_HEADER: Any
ARGS_LABEL: Any
ARGS_OPTIONS: Any
ARGS_SCRIPT: Any
ARGS_VERSION: Any

class _ColorDocoptExit(SystemExit):
    usage: str = ...
    def __init__(self, message: str = ...) -> None: ...

def _coloredhelp(s: Any): ...
def _docoptextras(help: Any, version: Any, options: Any, doc: Any) -> None: ...

_old_docopt: Any
