# (generated with --quick)

from typing import Any, List, NoReturn, Tuple

DatasetBase: Any
np: module
pickle: module

class InriaHoG(Any):
    _data_filename: Any
    _nr_neg_test: Any
    _nr_neg_train: Any
    _nr_pos_test: Any
    _nr_pos_train: Any
    def __init__(self, data_filename, nr_pos_train, nr_pos_test, nr_neg_train, nr_neg_test) -> None: ...
    @staticmethod
    def _normalise(data) -> NoReturn: ...
    def load_data(self) -> Tuple[Any, List[int], Any, List[int]]: ...

def test_inria_hog() -> None: ...
