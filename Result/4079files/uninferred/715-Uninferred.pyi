from ib_insync.contract import *
from typing import Any

class TkApp:
    ib: Any = ...
    root: Any = ...
    entry: Any = ...
    button: Any = ...
    text: Any = ...
    loop: Any = ...
    def __init__(self) -> None: ...
    def onButtonClick(self) -> None: ...
    def run(self) -> None: ...
    def _onTimeout(self) -> None: ...
    def _onDeleteWindow(self) -> None: ...

app: Any