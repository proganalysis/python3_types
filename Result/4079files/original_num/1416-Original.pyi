# (generated with --quick)

from typing import Any

base_file_handler: Any
base_output_handler: Any
sys: module

class OutputHandlerFile(Any):
    _OutputHandlerFile__confirm: bool
    _OutputHandlerFile__confirm_amount_same: int
    _OutputHandlerFile__confirm_counter: int
    _OutputHandlerFile__file_handler: Any
    _OutputHandlerFile__path: str
    _OutputHandlerFile__prompt_error: str
    _OutputHandlerFile__prompt_info: str
    _OutputHandlerFile__prompt_info_list: Any
    __doc__: str
    def Confirm(self, text: str, default = ..., abort = ...) -> bool: ...
    def PrintError(self, text: str) -> str: ...
    def PrintInfo(self, text: str) -> str: ...
    def PromptError(self, text: str) -> str: ...
    def PromptInfo(self, text: str) -> str: ...
    def PromptInfoWithDefault(self, text: str, text_type: object, default: object) -> str: ...
    def __init__(self, file_path: str, file_handler, prompt_info: str = ..., prompt_error: str = ..., confirm: bool = ..., confirm_amount_same: int = ..., prompt_info_list = ...) -> None: ...
