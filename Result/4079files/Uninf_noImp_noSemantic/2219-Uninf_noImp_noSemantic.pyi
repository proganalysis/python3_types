from typing import Any

_word_to_idx: Any
_idx_to_word: Any

def _add_word(word: Any): ...

UNKNOWN_WORD: str
START_WORD: str
END_WORD: str
UNKNOWN_TOKEN: Any
START_TOKEN: Any
END_TOKEN: Any

def look_up_word(word: Any): ...
def look_up_token(token: Any): ...

embeddings_path: Any
line: Any
chunks: Any
dimensions: Any
vocab_size: Any
glove: Any
idx: Any
