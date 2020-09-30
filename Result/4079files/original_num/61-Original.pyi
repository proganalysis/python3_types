# (generated with --quick)

from typing import Any, Dict, Union

AbstractWrapper: Any
logging: module
math: module
re: module
sys: module
wrapper: SGDWrapper

class SGDWrapper(Any):
    __doc__: str
    _return_value: None
    def __init__(self) -> None: ...
    def get_command_line_args(self, runargs, config) -> str: ...
    def process_results(self, filepointer, exit_code) -> Dict[str, Union[float, int, str]]: ...
