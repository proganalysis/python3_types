# (generated with --quick)

import contextlib
import ssl
from typing import Any, Optional, Tuple, Type, Union
import urllib.request
import xml.etree.ElementTree

DynamicObject: Any
__all__: Tuple[str, str]
_logger: logging.Logger
et: module
logging: module
report: FlexReport
suppress: Type[contextlib.suppress]
time: module
trades: list
util: Any

class FlexError(Exception): ...

class FlexReport:
    __doc__: str
    data: Any
    root: Optional[xml.etree.ElementTree.Element]
    def __init__(self, token = ..., queryId = ..., path = ...) -> None: ...
    def df(self, topic: str, parseNumbers = ...) -> Any: ...
    def download(self, token, queryId) -> None: ...
    def extract(self, topic: str, parseNumbers = ...) -> list: ...
    def load(self, path) -> None: ...
    def save(self, path) -> None: ...
    def topics(self) -> set: ...

def urlopen(url: Union[str, urllib.request.Request], data: Optional[bytes] = ..., timeout: Optional[float] = ..., *, cafile: Optional[str] = ..., capath: Optional[str] = ..., cadefault: bool = ..., context: Optional[ssl.SSLContext] = ...) -> Any: ...
