# (generated with --quick)

from typing import Any, Optional, Tuple

Configure: Any
LOG: logging.Logger
LOG_FORMAT: str
Login: Any
Session: Any
__version__: Any
argparse: module
get_session: Any
logging: module
sys: module

class Cli(object):
    COMMAND_CHOICES: Tuple[str, str]
    _account: Any
    _debug: bool
    _headless: bool
    _parsed_args: Optional[argparse.Namespace]
    _role: Any
    _session: Any
    args: Any
    def __init__(self, args = ...) -> None: ...
    def _configure(self) -> Any: ...
    def _create_parser(self) -> argparse.ArgumentParser: ...
    def _login(self) -> Any: ...
    def main(self) -> Any: ...

def main() -> Any: ...
