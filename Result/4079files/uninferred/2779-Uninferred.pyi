from typing import Any

logger: Any
SCRIPT_PATH: Any
APP_PATH: Any

class Script:
    path: Any = ...
    src: Any = ...
    _closed: bool = ...
    info: Any = ...
    def __init__(self, name: Any, set_dash_x: bool = ...) -> None: ...
    def close(self) -> None: ...
    def open(self) -> None: ...
    @property
    def tar(self): ...
    @property
    def source(self): ...
    def write(self, s: str = ..., newline: bool = ...) -> None: ...
    def write_all(self, commands: Any) -> None: ...

class Archive:
    workspace: Any = ...
    archive_file: Any = ...
    archive: Any = ...
    _closed: bool = ...
    exclude: Any = ...
    def __init__(self, workspace: Any) -> None: ...
    def add_script(self, script: Script) -> Any: ...
    def add_bundled_file(self, base: Any, path: Any) -> None: ...
    def _filter_git(self, info: Any): ...
    def add_project_file(self, path: Any) -> None: ...
    def close(self) -> None: ...
    def getfile(self): ...