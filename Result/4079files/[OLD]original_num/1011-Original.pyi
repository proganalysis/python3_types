# (generated with --quick)

import pathlib
from typing import Any, IO, Type

Path: Type[pathlib.Path]

def add_embeddings(keyed_vectors, *words, init = ...) -> Any: ...
def http_get(url: str, outfile: pathlib.Path, ignore_tardir = ...) -> None: ...
def http_get_temp(url: str, temp_file: IO) -> None: ...
def load_word2vec_file(word2vec_file, add_pad = ..., pad = ...) -> Any: ...
def sentencepiece_load(file) -> Any: ...
