# (generated with --quick)

from typing import List, Tuple, Union

cmd_changedir: str
cmd_files: str
cmd_path: str
file: Tuple[str, int]
fileList: List[Tuple[str, int]]
surfList: List[Tuple[str, int]]
sys: module

def readFileList() -> List[Tuple[str, int]]: ...
def runTecplotScript(fileList, surfList, cmd_changedir) -> None: ...
def system(command: Union[_PathLike, bytes, str]) -> int: ...
def updateTecplotMacro() -> None: ...
