from pathlib import Path
from typing import Any, IO, Optional

def sentencepiece_load(file: Any): ...
def http_get_temp(url: str, temp_file: IO) -> None: ...
def http_get(url: str, outfile: Path, ignore_tardir: Any=...) -> None: ...
def load_word2vec_file(word2vec_file: Any, add_pad: bool = ..., pad: str = ...): ...
def add_embeddings(keyed_vectors: Any, *words: Any, init: Optional[Any] = ...): ...