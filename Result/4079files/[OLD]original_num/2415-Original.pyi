# (generated with --quick)

import numpy
from typing import Any

CodeBlock: Any
Genome: Any
np: module

class Individual:
    __slots__ = ["_error_vector", "_error_vector_bytes", "_genome", "_program", "_total_error"]
    __doc__: str
    _error_vector: None
    _error_vector_bytes: None
    _genome: Any
    _program: None
    _total_error: Any
    error_vector: numpy.ndarray
    error_vector_bytes: Any
    genome: Any
    program: Any
    total_error: Any
    def __init__(self, genome = ...) -> None: ...
    def __lt__(self, other) -> Any: ...
