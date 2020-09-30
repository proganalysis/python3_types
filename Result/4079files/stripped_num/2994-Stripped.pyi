# (generated with --quick)

from typing import Any

SR: Any
Solver_algorithm: Any
np: module
root: Any

class Root(Any):
    _solution: Any
    def __init__(self) -> None: ...
    def _adapt_solution_to_solution_results(self) -> dict: ...
    def _get_equations_error(self, x, circuit) -> list: ...
    def solve(self, circuit, initial_conditions, **kwargs) -> dict: ...
