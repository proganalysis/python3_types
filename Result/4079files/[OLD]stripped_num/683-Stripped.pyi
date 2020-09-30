# (generated with --quick)

from typing import Any

json: module

class DbBackup(object):
    def dump_json(self, filepath, data) -> None: ...
    def load_json(self, filepath) -> Any: ...

class JsonBackupBody(object):
    files: Any
    def __init__(self, files = ...) -> None: ...
