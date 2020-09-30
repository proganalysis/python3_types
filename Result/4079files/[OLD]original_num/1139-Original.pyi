# (generated with --quick)

from typing import Any

gettext: Any
gridspec: Any
np: module
open_dataset: Any
plPoint: Any
plt: Any
seawater: Any
utils: Any

class TemperatureSalinityPlotter(Any):
    plottype: str
    time: Any
    timestamp: Any
    def __init__(self, dataset_name: str, query: str, format: str) -> None: ...
    def csv(self) -> Any: ...
    def load_data(self) -> None: ...
    def plot(self) -> Any: ...
