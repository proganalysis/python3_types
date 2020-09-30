# (generated with --quick)

import __future__
from typing import Any, Tuple

KNOWN_WAVE_FORMATS: Tuple[int, int]
WAVE_FORMAT_EXTENSIBLE: int
WAVE_FORMAT_IEEE_FLOAT: int
WAVE_FORMAT_PCM: int
_big_endian: bool
absolute_import: __future__._Feature
division: __future__._Feature
numpy: module
print_function: __future__._Feature
struct: module
sys: module
warnings: module

class WavFileWarning(UserWarning): ...

def _array_tofile(fid, data) -> None: ...
def _read_data_chunk(fid, comp, noc, bits, mmap = ...) -> Any: ...
def _read_fmt_chunk(fid) -> Tuple[Any, Any, Any, Any, Any, Any, Any]: ...
def _read_riff_chunk(fid) -> Any: ...
def _skip_unknown_chunk(fid) -> None: ...
def read(filename, mmap = ...) -> Tuple[Any, Any]: ...
def write(filename, rate, data) -> None: ...
