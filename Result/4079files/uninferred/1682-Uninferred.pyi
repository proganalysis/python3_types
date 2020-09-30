from typing import Any

META_GRAPH_FILE: str
WEIGHTS_FILE: str
NUM_HIDDEN_LAYERS: int
GRU_INTERNAL_SIZE: int

class CharPrinter:
    _max_line_length: Any = ...
    _num_chars_on_current_line: int = ...
    def __init__(self, max_line_length: int=...) -> None: ...
    def print_char(self, ch: str) -> Any: ...

initial_char: Any
printer: Any
new_saver: Any
x: Any
h: Any
yo: Any
ch: Any
