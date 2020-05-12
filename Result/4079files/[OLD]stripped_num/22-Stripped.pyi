# (generated with --quick)

from typing import Any, List, TypeVar, Union

numpy: module
random: module
time: module

_TLogistic = TypeVar('_TLogistic', bound=Logistic)

class Logistic:
    _dataIn: Union[numpy.ndarray, List[nothing]]
    _labels: Any
    _w: Any
    def __init__(self) -> None: ...
    def _sigmoid(self, inX) -> Any: ...
    def classify(self, inX) -> int: ...
    def fit(self: _TLogistic, dataSet, labels, trainN, alpha = ..., printTime = ...) -> _TLogistic: ...
