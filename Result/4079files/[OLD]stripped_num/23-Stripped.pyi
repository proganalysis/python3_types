# (generated with --quick)

from typing import Any

ContextMenuCombined: Any
EosDrone: Any
EosFighter: Any
EosFit: Any
EosModule: Any
Fit: Any
cmd: Any
getSimilarFighters: Any
getSimilarModPositions: Any
gui: Any
math: module
wx: Any

class RemoveItem(Any):
    mainFrame: Any
    srcContext: Any
    def _RemoveItem__handleBooster(self, callingWindow, mainItem, selection) -> None: ...
    def _RemoveItem__handleCargo(self, callingWindow, mainItem, selection) -> None: ...
    def _RemoveItem__handleCommandFit(self, callingWindow, mainItem, selection) -> None: ...
    def _RemoveItem__handleDrone(self, callingWindow, mainItem, selection) -> None: ...
    def _RemoveItem__handleFighter(self, callingWindow, mainItem, selection) -> None: ...
    def _RemoveItem__handleGraphItem(self, callingWindow, mainItem, selection) -> None: ...
    def _RemoveItem__handleImplant(self, callingWindow, mainItem, selection) -> None: ...
    def _RemoveItem__handleModule(self, callingWindow, mainItem, selection) -> None: ...
    def _RemoveItem__handleProjectedItem(self, callingWindow, mainItem, selection) -> None: ...
    def __init__(self) -> None: ...
    def activate(self, callingWindow, fullContext, mainItem, selection, i) -> None: ...
    def display(self, callingWindow, srcContext, mainItem, selection) -> bool: ...
    def getText(self, callingWindow, itmContext, mainItem, selection) -> str: ...
