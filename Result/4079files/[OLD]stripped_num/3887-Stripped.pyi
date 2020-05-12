# (generated with --quick)

from typing import Any, Dict, List, Union

CONSOLE_LOGGING: Dict[str, Union[int, Dict[str, Union[str, Dict[str, Any], List[str]]]]]
FILE_CONSOLE_LOGGING: Dict[str, Union[int, Dict[str, Union[str, Dict[str, Any], List[str]]]]]
FILE_LOGGING: Dict[str, Union[int, Dict[str, Union[str, Dict[str, Any], List[str]]]]]
FORMATTERS: Dict[str, Dict[str, str]]
LOGGING_CONFIGS: Dict[str, Dict[str, Union[int, Dict[str, Union[str, Dict[str, Any], List[str]]]]]]
NO_LOGGING: Dict[str, int]
logging: module
sys: module

def is_python34() -> bool: ...
def log_mxnet_version(logger) -> None: ...
def log_sockeye_version(logger) -> None: ...
def setup_main_logger(file_logging = ..., console = ..., path = ..., level = ...) -> None: ...
