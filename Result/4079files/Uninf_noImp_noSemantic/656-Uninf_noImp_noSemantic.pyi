from TouchStyle import *
from TouchAuxiliary import *
from typing import Any

__author__: str
__email__: str
__status__: str

class TouchGuiApplication(TouchApplication):
    status: str = ...
    window: Any = ...
    mainBox: Any = ...
    subBoxA: Any = ...
    listWidget: Any = ...
    button: Any = ...
    def __init__(self, args: Any) -> None: ...
    def executeButtonClick(self) -> None: ...
    def runProgram(self, programName: Any) -> None: ...
