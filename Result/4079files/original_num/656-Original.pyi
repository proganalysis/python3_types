# (generated with --quick)

import roProgram
from typing import Any, List, Optional, Type, Union

RoboProProgram: Type[roProgram.RoboProProgram]
__author__: str
__email__: str
__status__: str
os: module

class TouchGuiApplication(Any):
    button: Any
    listWidget: Any
    mainBox: Any
    status: str
    subBoxA: Any
    window: Any
    def __init__(self, args) -> None: ...
    def executeButtonClick(self) -> None: ...
    def runProgram(self, programName) -> None: ...

def __getattr__(name) -> Any: ...
@overload
def osList(path: bytes) -> List[bytes]: ...
@overload
def osList(path: Optional[str] = ...) -> List[str]: ...
@overload
def osList(path: Union[int, _PathLike[str]]) -> List[str]: ...
