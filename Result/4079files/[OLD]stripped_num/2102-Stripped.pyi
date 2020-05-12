# (generated with --quick)

from typing import Any, Dict, Union

Atmosphere: Any
argparse: module
args: Dict[str, Any]
choices: list
config: Any
np: module
opts: Dict[str, Any]
sys: module

def _parser() -> argparse.Namespace: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def main(bands = ..., verbose = ...) -> None: ...
