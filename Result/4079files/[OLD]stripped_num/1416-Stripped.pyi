# (generated with --quick)

from typing import Any

base_file_handler: Any
base_output_handler: Any
sys: module

class OutputHandlerFile(Any):
    _OutputHandlerFile__confirm: Any
    _OutputHandlerFile__confirm_amount_same: Any
    _OutputHandlerFile__confirm_counter: int
    _OutputHandlerFile__file_handler: Any
    _OutputHandlerFile__path: Any
    _OutputHandlerFile__prompt_error: Any
    _OutputHandlerFile__prompt_info: Any
    _OutputHandlerFile__prompt_info_list: Any
    __doc__: str
    def Confirm(self, text, default = ..., abort = ...) -> Any: ...
    def PrintError(self, text) -> Any: ...
    def PrintInfo(self, text) -> Any: ...
    def PromptError(self, text) -> Any: ...
    def PromptInfo(self, text) -> Any: ...
    def PromptInfoWithDefault(self, text, text_type, default) -> Any: ...
    def __init__(self, file_path, file_handler, prompt_info = ..., prompt_error = ..., confirm = ..., confirm_amount_same = ..., prompt_info_list = ...) -> None: ...
