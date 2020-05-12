# (generated with --quick)

from typing import IO, Optional, Union

class Console:
    input_reader: IO[Union[bytes, str]]
    output_writer: IO[Union[bytes, str]]
    def __init__(self, input_reader: IO, output_writer: IO) -> None: ...
    def input(self, prompt: Optional[str] = ...) -> str: ...
    def print(self, string: Optional[str] = ..., end: str = ..., flush: bool = ...) -> None: ...
