# (generated with --quick)

from typing import Any

LOG: logging.Logger
logging: module
o: Any
time: module

class Overpass(object):
    _Overpass__api: Any
    def __init__(self, uri = ...) -> None: ...
    def request_with_retries(self, request, output_format = ...) -> Any: ...
