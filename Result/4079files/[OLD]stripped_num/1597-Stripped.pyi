# (generated with --quick)

from typing import Any, Optional

SigninViewModel: Any

class RegisterViewModel(Any):
    confirm_password: Any
    error: Optional[str]
    def __init__(self) -> None: ...
    def from_dict(self, data_dict) -> None: ...
    def validate(self) -> None: ...
