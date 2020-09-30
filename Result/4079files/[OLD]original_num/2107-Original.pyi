# (generated with --quick)

from typing import Any, Dict, List, Optional

CURRENT_DIR: str
Command: Any
Store: Any
argparse: module
inspect: module
logging: module
os: module
pkgutil: module
sys: module

class BaseManage(object):
    _commands: Optional[List[str]]
    _logger: Optional[logging.Logger]
    _modules: Dict[str, Any]
    commands: Any
    commands_package_path: Optional[str]
    config: Dict[nothing, nothing]
    debug: Any
    logger: Any
    store_cls: Any
    def _parse_manage_arguments(self) -> argparse.Namespace: ...
    def _run_command(self, command, *args) -> None: ...
    def help(self) -> None: ...
    def run(self) -> Optional[int]: ...

def main(manager_cls) -> None: ...
