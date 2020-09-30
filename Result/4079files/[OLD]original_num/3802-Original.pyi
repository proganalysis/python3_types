# (generated with --quick)

import click.core
from typing import Any, Dict, List, Optional

WrfRunnerException: Any
arrow: Any
click: module
glob: module
main: click.core.Command
os: module
re: module

class NAM:
    data_files: Optional[list]
    dataset_end: Any
    dataset_start: Any
    dates: Optional[Dict[Any, list]]
    dx: int
    folder: Any
    time_step: int
    def __init__(self, folder) -> None: ...
    def check_complete(self) -> None: ...
    @staticmethod
    def filename_to_datetime(filename) -> Any: ...
    def scan_folder(self) -> None: ...

class NAM_forecast:
    data_files: Optional[List[str]]
    dataset_end: Any
    dataset_start: Any
    dates: Any
    dx: int
    folder: str
    time_step: int
    def __init__(self, folder) -> None: ...
    @staticmethod
    def filename_to_datetime(filename) -> Any: ...
    def scan_folder(self) -> None: ...
