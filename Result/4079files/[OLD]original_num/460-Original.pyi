# (generated with --quick)

from typing import Any

QtCore: Any
QtGui: Any
configPath: str
os: module
sys: module
time: module
traceback: module

class SpecificWorker(Any):
    Period: int
    compute: Any
    def __init__(self, proxy_map) -> None: ...
    def setImage(self, img) -> None: ...
    def setImageFromFile(self, pathImg) -> None: ...
    def setParams(self, params) -> bool: ...

def __getattr__(name) -> Any: ...
