# (generated with --quick)

from typing import Any

DEFAULT_CONFIG_FILE: Any
os: module
shutil: module
yaml: Any

class Config(object):
    _config: Any
    _path: Any
    _protect_rewrites: Any
    pathdir: Any
    def __contains__(self, key) -> bool: ...
    def __delitem__(self, key) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __getattr__(self, key) -> Any: ...
    def __getitem__(self, key) -> Any: ...
    def __init__(self, path) -> None: ...
    def __setattr__(self, key, value) -> None: ...
    def __setitem__(self, key, value) -> Any: ...
    def _rewrite(self) -> None: ...
    def change_file(self, filename) -> None: ...
    def copy_file(self, directory = ..., switch = ...) -> None: ...
    def get_pathdir(self) -> Any: ...
    def update(self, d = ..., **kwargs) -> None: ...
