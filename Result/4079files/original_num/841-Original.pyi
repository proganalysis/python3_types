# (generated with --quick)

from typing import Any

Panel: Any
QConnectionView: Any
QMatrixView: Any
QWidget: Any
np: module

class ExperimentsPanel(Any):
    __doc__: str
    _data: Any
    _layer: Any
    _network: Any
    connections_view: Any
    matrix_view: Any
    def __init__(self, parent = ...) -> None: ...
    def initUI(self) -> None: ...
    def setInputData(self, data = ...) -> None: ...
    def setLayer(self, layer = ...) -> None: ...
    def setNetwork(self, network = ...) -> None: ...
    def updateActivation(self) -> None: ...
