# (generated with --quick)

import pathlib
from typing import Any, Callable, Dict, Generator, List, SupportsFloat, Type

ACCURACY_THRESHOLDS: List[int]
CHUNK_PROPORTION: float
CHUNK_SIZE: int
CONTENT_SIZE: Any
DataSet: Any
FITTING_FACTOR: int
GuesslangError: Any
LOGGER: logging.Logger
NEURAL_NETWORK_HIDDEN_LAYERS: List[int]
OPTIMIZER_STEP: float
Path: Type[pathlib.Path]
config_dict: Any
extract: Any
extract_from_files: Any
gc: module
logging: module
model_info: Any
safe_read_file: Any
search_files: Any
tf: Any

class Guess:
    __doc__: str
    _classifier: Any
    is_default: Any
    languages: Any
    model_dir: Any
    def __init__(self, model_dir = ...) -> None: ...
    def language_name(self, text) -> Any: ...
    def learn(self, input_dir) -> Any: ...
    def probable_languages(self, text, max_languages = ...) -> Any: ...
    def scores(self, text) -> dict: ...
    def test(self, input_dir) -> Dict[str, Any]: ...

def _comment(accuracy) -> None: ...
def _pop_many(items, chunk_size) -> Generator[Any, Any, None]: ...
def _to_func(vector) -> Callable[[], Any]: ...
def ceil(__x: SupportsFloat) -> int: ...
def itemgetter(*items) -> Callable[[Any], tuple]: ...
def log(x: SupportsFloat, base: SupportsFloat = ...) -> float: ...
