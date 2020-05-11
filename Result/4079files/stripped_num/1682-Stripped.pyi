# (generated with --quick)

import numpy
from typing import Any

GRU_INTERNAL_SIZE: int
META_GRAPH_FILE: str
NUM_HIDDEN_LAYERS: int
WEIGHTS_FILE: str
ch: Any
convert_from_alphabet: Any
convert_to_alphabet_int: Any
convert_to_alphabet_str: Any
h: Any
i: int
initial_char: Any
new_saver: Any
np: module
printer: CharPrinter
sample_from_probabilities: Any
session: Any
tf: Any
x: numpy.ndarray
yo: Any

class CharPrinter:
    _max_line_length: Any
    _num_chars_on_current_line: int
    def __init__(self, max_line_length = ...) -> None: ...
    def print_char(self, ch) -> None: ...
