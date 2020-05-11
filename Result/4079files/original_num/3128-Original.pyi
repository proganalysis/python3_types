# (generated with --quick)

import numpy
from typing import Any, NoReturn, Tuple

DatasetBase: Any
np: module
pickle: module

class InriaHoG(Any):
    _data_filename: str
    _nr_neg_test: int
    _nr_neg_train: int
    _nr_pos_test: int
    _nr_pos_train: int
    def __init__(self, data_filename: str, nr_pos_train: int, nr_pos_test: int, nr_neg_train: int, nr_neg_test: int) -> None: ...
    @staticmethod
    def _normalise(data: numpy.ndarray) -> NoReturn: ...
    def load_data(self) -> Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray, numpy.ndarray]: ...

def test_inria_hog() -> None: ...
