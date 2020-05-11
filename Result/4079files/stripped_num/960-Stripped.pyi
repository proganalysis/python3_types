# (generated with --quick)

from typing import Any, Dict, NoReturn, TypeVar

csr_matrix: Any
lazy_method: Any
linalg: Any
mathcollection: MathCollection
np: module
svd: Any

_T0 = TypeVar('_T0')

class BaseStatModel:
    N: Any
    _raw_train_x: Any
    _raw_train_y: Any
    _x_mean_: Any
    _x_std_: Any
    do_standardization: Any
    features_name: Any
    math: MathCollection
    p: Any
    train_x: Any
    train_y: Any
    def __init__(self, train_x, train_y, features_name = ..., do_standardization = ...) -> None: ...
    def _pre_processing_x(self, X: _T0) -> _T0: ...
    def _pre_processing_y(self, y: _T0) -> _T0: ...
    def pre_processing(self) -> None: ...
    def predict(self, X) -> NoReturn: ...
    def standardize(self, x, axis = ..., with_mean = ..., with_std = ...) -> Any: ...
    def test(self, X, y) -> NoReturn: ...
    def train(self) -> NoReturn: ...

class ClassificationMixin(BaseStatModel):
    _get_unique_sorted_label: Any
    _label_map: Dict[nothing, nothing]
    _raw_train_x: Any
    _raw_train_y: Any
    _x_mean_: None
    _x_std_: None
    do_standardization: bool
    features_name: None
    n_class: Any
    train_x: Any
    train_y: Any
    def __init__(self, *args, n_class = ..., **kwargs) -> None: ...
    def _inverse_matrix_to_class(self, matrix) -> Any: ...
    def _pre_processing_y(self, y) -> Any: ...

class MathCollection:
    inv: Any
    pinv: Any
    sum: Any
    svd: Any
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...

class Result:
    N: Any
    error_rate: Any
    mse: Any
    prediction_error: Any
    std_error: Any
    y: Any
    y_hat: Any
    def __init__(self, y_hat, y) -> None: ...
