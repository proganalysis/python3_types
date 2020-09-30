# (generated with --quick)

import collections
from typing import Any, Type

FILE_PREFIX: collections.defaultdict[str, Any]
QObject: Any
defaultdict: Type[collections.defaultdict]
pyqtProperty: Any
pyqtSignal: Any
pyqtSlot: Any

class FileIO(Any):
    _source: str
    read: Any
    source: Any
    sourceChanged: Any
    write: Any
    def __init__(self, parent) -> None: ...
    @staticmethod
    def removeFilePrefix(path) -> Any: ...

def system() -> str: ...
