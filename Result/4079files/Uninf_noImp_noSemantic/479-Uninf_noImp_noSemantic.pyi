from coalib.results.Result import Result
from coalib.results.result_actions.ResultAction import ResultAction
from typing import Any

class PrintDebugMessageAction(ResultAction):
    @staticmethod
    def is_applicable(result: Result, original_file_dict: Any, file_diff_dict: Any, applied_actions: Any=...) -> Any: ...
    def apply(self, result: Any, original_file_dict: Any, file_diff_dict: Any): ...
