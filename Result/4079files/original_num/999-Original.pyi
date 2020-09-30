# (generated with --quick)

import json.encoder
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union

sys: module
tqdm: Any

class Output:
    porcelain: Any
    progress_bars: Dict[Any, Dict[str, Any]]
    silent: Any
    verbosity: Any
    @staticmethod
    def add_progress_bar(id, desc, unit = ...) -> None: ...
    @staticmethod
    def exception(exception) -> None: ...
    @staticmethod
    def initialize(porcelain = ..., silent = ..., verbosity = ...) -> None: ...
    @staticmethod
    def message(message, *args) -> None: ...
    @staticmethod
    def update_progress_bar(id, remaining = ...) -> None: ...

def dumps(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
def print_json_patch(json) -> None: ...
