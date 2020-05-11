# (generated with --quick)

import json.encoder
import threading
from typing import Any, Callable, Optional, Tuple, Type, Union

Thread: Type[threading.Thread]

class PayloadViewerThread(threading.Thread):
    _PayloadViewerThread__payload: None
    __doc__: str
    payload: Any
    refreshable: bool
    running: bool
    def __init__(self) -> None: ...
    def refresh(self) -> None: ...
    def run(self) -> Any: ...
    def shutdown(self) -> None: ...

def dumps(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
