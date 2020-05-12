# (generated with --quick)

import base
from typing import Any, Type

QAbstractItemView: Any
QFrame: Any
QHBoxLayout: Any
QLabel: Any
QPushButton: Any
QTableWidget: Any
QVBoxLayout: Any
ScrollArea: Type[base.ScrollArea]
__author__: str

class DownloadFrame(base.ScrollArea):
    currentStorageFolder: Any
    currentStorageFolderLabel: Any
    mainLayout: Any
    parent: Any
    selectButton: Any
    singsTable: Any
    spaceLine: Any
    topShowLayout: Any
    def setHeader(self) -> None: ...
    def setMusicTable(self) -> None: ...
