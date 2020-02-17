# (generated with --quick)

import pathlib
from typing import Any, Callable, Dict, Iterator, List, Optional, SupportsFloat, Tuple, Type

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
    def __init__(self, model_dir: Optional[str] = ...) -> None: ...
    def language_name(self, text: str) -> str: ...
    def learn(self, input_dir: str) -> float: ...
    def probable_languages(self, text: str, max_languages: int = ...) -> Tuple[str, ...]: ...
    def scores(self, text: str) -> Dict[str, float]: ...
    def test(self, input_dir: str) -> Dict[str, Any]: ...

def _comment(accuracy: float) -> None: ...
def _pop_many(items: List[pathlib.Path], chunk_size: int) -> Iterator[List[pathlib.Path]]: ...
def _to_func(vector) -> Callable[[], Tuple[Any, Any]]: ...
def ceil(__x: SupportsFloat) -> int: ...
def itemgetter(*items) -> Callable[[Any], tuple]: ...
def log(x: SupportsFloat, base: SupportsFloat = ...) -> float: ...
