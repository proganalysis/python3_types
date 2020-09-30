# (generated with --quick)

from typing import Any, Dict, Tuple

OnlineAffineExpansionStorage: Any
all_product: Dict[str, Any]
all_sum: Dict[str, Any]
factory_product: Any
factory_sum: Any
isclose: Any
norm: Any
numpy_product: Any
numpy_sum: Any
online_product: Any
online_sum: Any
product: Any
pytest: Any
sum: Any
test_numpy_vector_assembly: Any

class Data(object):
    N: Any
    Q: Any
    def __init__(self, N, Q) -> None: ...
    def assert_backend(self, theta, F, result_backend) -> None: ...
    def evaluate_backend(self, theta, F) -> Any: ...
    def evaluate_builtin(self, theta, F) -> Any: ...
    def generate_random(self) -> Tuple[Any, Any]: ...

def RandomNumpyVector(N) -> Any: ...
def RandomTuple(Q) -> Any: ...
