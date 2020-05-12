# (generated with --quick)

import shutil
from typing import Dict, List, TextIO, Type, Union

SUPPRESS: str
stderr: TextIO
valid_args: Dict[str, Dict[str, Union[int, str, List[Union[int, str]], Type[int]]]]

def add_arguments(parser, selected_args = ...) -> None: ...
def disk_usage(path: Union[str, _PathLike[str]]) -> shutil._ntuple_diskusage: ...
def disk_usage_info(wd, keep_free, warn = ..., quiet = ...) -> None: ...
def makedirs(name: Union[_PathLike, bytes, str], mode: int = ..., exist_ok: bool = ...) -> None: ...
