# (generated with --quick)

from typing import Any, Tuple, TypeVar, Union

BLACK: Any
BaseLearn: Any
Dense: Any
Dropout: Any
EMPTY: Any
Sequential: Any
WHITE: Any
np: module
sqlite3: module
to_categorical: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class Learn(Any):
    data_retrieval_command: str
    training_size: int
    def __init__(self) -> None: ...
    def get_path_to_self(self) -> str: ...
    def handle_data(self, training_data) -> Tuple[Any, Any]: ...
    def setup_and_compile_model(self) -> Any: ...
    def train(self, model, X, Y) -> None: ...

def abspath(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
