# (generated with --quick)

from typing import Any, Union

cmd_changedir: str
cmd_files: str
cmd_path: str
file: Any
fileList: list
surfList: list
sys: module

def readFileList() -> list: ...
def runTecplotScript(fileList: list, surfList: list, cmd_changedir: str) -> None: ...
def system(command: Union[_PathLike, bytes, str]) -> int: ...
def updateTecplotMacro() -> None: ...
