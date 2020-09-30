# (generated with --quick)

import __future__
import typing
from typing import Any, Dict, Generator, Tuple, Type

Counter: Type[typing.Counter]
DATA_FOLDER: str
DOWNLOAD_URL: str
EXPECTED_BYTES: int
FILE_NAME: str
absolute_import: __future__._Feature
division: __future__._Feature
np: module
os: module
print_function: __future__._Feature
random: module
tf: Any
urllib: module
zipfile: module

def build_vocab(words, vocab_size) -> Tuple[Dict[str, int], Dict[int, str]]: ...
def convert_words_to_index(words, dictionary) -> list: ...
def download(file_name, expected_bytes) -> str: ...
def generate_sample(index_words, context_window_size) -> Generator[Tuple[Any, Any], Any, None]: ...
def get_batch(iterator, batch_size) -> Generator[Tuple[Any, Any], Any, Any]: ...
def get_index_vocab(vocab_size) -> Tuple[Dict[str, int], Dict[int, str]]: ...
def process_data(vocab_size, batch_size, skip_window) -> Generator[Tuple[Any, Any], Any, Any]: ...
def read_data(file_path) -> Any: ...
