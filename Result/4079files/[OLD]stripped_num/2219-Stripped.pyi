# (generated with --quick)

import numpy
from typing import Any, Dict, List, TextIO

END_TOKEN: int
END_WORD: str
START_TOKEN: int
START_WORD: str
UNKNOWN_TOKEN: int
UNKNOWN_WORD: str
_idx_to_word: list
_word_to_idx: Dict[Any, int]
chunks: List[str]
dimensions: int
embeddings_path: str
f: TextIO
glove: numpy.ndarray
idx: int
line: str
np: module
os: module
vocab_size: int

def _add_word(word) -> int: ...
def look_up_token(token) -> Any: ...
def look_up_word(word) -> int: ...
