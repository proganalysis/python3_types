# (generated with --quick)

import functools
import typing
from typing import Any, Callable, Iterable, List, Tuple, Type, TypeVar, Union

Counter: Type[typing.Counter]
beta: Any
beta_0: List[int]
beta_hat: Any
data: List[list]
false_negatives: int
false_positives: int
fn: functools.partial[nothing]
gradient_fn: functools.partial[nothing]
math: module
partial: Type[functools.partial]
precision: float
predict: Union[Callable[[Any, Any], Any], float]
random: module
recall: float
rescale: Any
rescaled_x: Any
true_negatives: int
true_positives: int
x: List[list]
x_i: Any
x_test: Any
x_train: Any
y: list
y_i: Any
y_test: Any
y_train: Any

_S = TypeVar('_S')
_T = TypeVar('_T')

def dot(v, w) -> Any: ...
def estimate_beta(x, y) -> Any: ...
def logistic(x) -> float: ...
def logistic_log_gradient(x, y, beta) -> Any: ...
def logistic_log_gradient_i(x_i, y_i, beta) -> list: ...
def logistic_log_likelihood(x, y, beta) -> Any: ...
def logistic_log_likelihood_i(x_i, y_i, beta) -> float: ...
def logistic_log_partial_ij(x_i, y_i, beta, j) -> Any: ...
def logistic_prime(x) -> float: ...
def maximize_batch(target_fn, gradient_fn, theta_0, tolerance = ...) -> Any: ...
def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0 = ...) -> Any: ...
@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
def train_test_split(x, y, test_pct) -> Tuple[Any, Any, Any, Any]: ...
def vector_add(v, w) -> Any: ...
