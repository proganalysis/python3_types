# (generated with --quick)

from typing import Any, Optional

cli: Any
container: Any
docker: Any
logging: module
pydev_docker: Any
sys: module
utils: Any

class CommandDispatcher:
    _REGISTRY: Any
    __doc__: str
    _pydev_container: Any
    run: Any
    run_pty: Any
    def __init__(self, pydev_container) -> None: ...
    def dispatch(self, command, options) -> Any: ...

class DispatcherError(Error):
    __doc__: str

class Error(Exception):
    __doc__: str

def main() -> Optional[int]: ...
def print_exception(msg) -> None: ...
def setup_logger(verbosity) -> None: ...
