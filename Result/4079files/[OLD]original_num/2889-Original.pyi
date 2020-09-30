# (generated with --quick)

from typing import Any, Iterable, Iterator, Tuple

EncoderBase: Any
logging: module
numpy: module
sklearn: Any
typing: module

class ITQEncoder(Any):
    TrainedITQEncoder: type
    iteration: int
    num_bit: int
    trained_encoder: Any
    def _ITQEncoder__fit(self, data, bits, iteration) -> Any: ...
    def _ITQEncoder__preprocess(self, data, bits) -> Tuple[Any, Any]: ...
    def __init__(self, iteration: int = ..., num_bit: int = ...) -> None: ...
    def fit(self, x_train) -> None: ...
    def inverse_transform_generator(self, x_test: Iterable[Iterator[int]]) -> Any: ...
    def transform_generator(self, x_test: Iterable[Iterator[float]]) -> Any: ...
