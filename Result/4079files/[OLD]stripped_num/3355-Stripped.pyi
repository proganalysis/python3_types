# (generated with --quick)

from typing import Any

BitmapLoader: Any
Fit: Any
MarketPriceSettings: Any
Price: Any
StatsView: Any
formatAmount: Any
wx: Any

class PriceViewFull(Any):
    fit: Any
    headerPanel: Any
    labelEMStatus: Any
    name: str
    panel: Any
    parent: Any
    settings: Any
    def __init__(self, parent) -> None: ...
    def getHeaderText(self, fit) -> str: ...
    def populatePanel(self, contentPanel, headerPanel) -> None: ...
    def processPrices(self, prices) -> None: ...
    def refreshPanel(self, fit) -> None: ...
    def refreshPanelPrices(self, fit = ...) -> None: ...
