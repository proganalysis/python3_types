# (generated with --quick)

from typing import Any, Union

config: Any
json: module

def exists(path: Union[_PathLike, bytes, int, str]) -> bool: ...
def load_config(path) -> None: ...
def save_config(path, config) -> None: ...
