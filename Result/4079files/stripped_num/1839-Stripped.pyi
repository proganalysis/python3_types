# (generated with --quick)

from typing import Any, Tuple, TypeVar, Union

_logsubexp: Any
_meanVarToBeta: Any
np: module

_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')

def predictRecallMedian(prior, tnow, percentile = ...) -> Any: ...
def predictRecallMode(prior, tnow) -> Any: ...
def predictRecallMonteCarlo(prior, tnow, N = ...) -> dict: ...
def updateRecallMonteCarlo(prior, result, tnow: _T2, tback: _T3 = ..., N = ...) -> Tuple[Any, Any, Union[_T2, _T3]]: ...
