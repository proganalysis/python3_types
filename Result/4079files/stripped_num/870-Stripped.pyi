# (generated with --quick)

from typing import Any, List, Optional, SupportsFloat, Union

argparse: module
args: argparse.Namespace
draw_f1_lines: Any
parser: argparse.ArgumentParser
path: module
plt: Any
re: module

class Sample:
    f1: float
    p: float
    r: float
    t1: float
    t2: float
    def __init__(self, line) -> None: ...

def ceil(__x: SupportsFloat) -> int: ...
@overload
def listdir(path: bytes) -> List[bytes]: ...
@overload
def listdir(path: Optional[str] = ...) -> List[str]: ...
@overload
def listdir(path: Union[int, _PathLike[str]]) -> List[str]: ...
def main(input, output) -> None: ...
def sqrt(__x: SupportsFloat) -> float: ...
