# (generated with --quick)

from typing import Any, TypeVar

Result: Any
ResultAction: Any
enforce_signature: Any

_T2 = TypeVar('_T2')

class PrintDebugMessageAction(Any):
    is_applicable: Any
    def apply(self, result, original_file_dict, file_diff_dict: _T2) -> _T2: ...
