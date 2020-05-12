# (generated with --quick)

from typing import Any, Sequence

Ryxxy: Any
cirq: Any
givens_matrix_elements: Any
givens_rotate: Any
numpy: module

class GivensMatrixError(Exception): ...

class GivensTranspositionError(Exception): ...

def optimal_givens_decomposition(qubits: Sequence, unitary: numpy.ndarray) -> Any: ...
