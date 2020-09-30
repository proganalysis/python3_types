# (generated with --quick)

from typing import Any, Generator, Tuple

Comment: Any
Comments: Any
Format: Any
Pipe: Any
Video: Any

class Custom(Any):
    def __init__(self, video, format_name: str) -> None: ...
    def comment_generator(self, comments) -> Generator[Tuple[str, Any], None, None]: ...
    def use(self) -> Tuple[Generator[Tuple[str, Any], None, None], str]: ...
