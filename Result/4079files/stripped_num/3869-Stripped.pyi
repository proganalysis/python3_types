# (generated with --quick)

import _importlib_modulespec
from typing import Any

json: module
logger: Any
os: module
pytest: Any
queue: Any
serve: Any
server_subprocesses: Any
tempfile: module
tempfile_name: Any
threading: module

class ServerProcSpy(Any):
    instances: None
    def start(self, *args, **kwargs) -> Any: ...

def reload(module: _importlib_modulespec.ModuleType) -> _importlib_modulespec.ModuleType: ...
def test_subprocess_exit(server_subprocesses, tempfile_name) -> None: ...
