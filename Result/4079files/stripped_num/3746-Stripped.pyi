# (generated with --quick)

import numpy
from typing import Any, Generator, Tuple

np: module
sp: Any

class ShuffleSplit(object):
    n_iter: Any
    random_state: Any
    train_size: Any
    def __init__(self, n_iter = ..., train_size = ..., random_state = ...) -> None: ...
    def __len__(self) -> Any: ...
    def split(self, X) -> Generator[Tuple[Any, Any], Any, None]: ...

def cross_val_score(estimator, X, cv) -> numpy.ndarray: ...
def train_test_split(X, train_size = ..., random_state = ...) -> Tuple[Any, Any]: ...
