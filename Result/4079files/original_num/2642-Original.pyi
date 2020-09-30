# (generated with --quick)

from typing import Any, Tuple, TypeVar

BaseEstimator: Any
DictFact: Any
Memory: Any
Parallel: Any
check_random_state: Any
copy: module
delayed: Any
np: module
torch: Any

_TEnsembleClassifier = TypeVar('_TEnsembleClassifier', bound=EnsembleClassifier)

class EnsembleClassifier(Any):
    alpha: Any
    estimator: Any
    estimator_: Any
    memory: Any
    n_jobs: Any
    n_runs: Any
    seed: Any
    warmup: Any
    def __init__(self, estimator, n_jobs = ..., seed = ..., n_runs = ..., alpha = ..., memory = ..., warmup = ...) -> None: ...
    def fit(self: _TEnsembleClassifier, X, y, callback = ...) -> _TEnsembleClassifier: ...
    def predict(self, X) -> Any: ...

def _compute_coefs(estimator, X, y, seed = ...) -> Tuple[Any, dict, Any]: ...
def _compute_components(embedder_weights, embedder_init, alpha, warmup) -> Any: ...
