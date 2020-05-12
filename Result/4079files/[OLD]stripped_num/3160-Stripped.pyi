# (generated with --quick)

import __future__
from typing import Any, List, NoReturn

OptimizeResult: Any
__all__: List[nothing]
_check_unknown_options: Any
_status_message: Any
absolute_import: __future__._Feature
division: __future__._Feature
math: module
np: module
print_function: __future__._Feature
scipy: Any
wrap_function: Any

class BaseQuadraticSubproblem(object):
    __doc__: str
    _cauchy_point: None
    _f: Any
    _g: Any
    _g_mag: None
    _h: Any
    _newton_point: None
    _x: Any
    fun: Any
    hess: Any
    jac: Any
    jac_mag: Any
    def __call__(self, p) -> Any: ...
    def __init__(self, x, fun, jac, hess = ..., hessp = ...) -> None: ...
    def _fun(self, _1) -> Any: ...
    def _hess(self, _1) -> Any: ...
    def _hessp(self, _1, _2) -> Any: ...
    def _jac(self, _1) -> Any: ...
    def get_boundaries_intersections(self, z, d, trust_radius) -> list: ...
    def hessp(self, p) -> Any: ...
    def solve(self, trust_radius) -> NoReturn: ...

def _minimize_trust_region(fun, x0, args = ..., jac = ..., hess = ..., hessp = ..., subproblem = ..., initial_trust_radius = ..., max_trust_radius = ..., eta = ..., gtol = ..., maxiter = ..., disp = ..., return_all = ..., callback = ..., inexact = ..., **unknown_options) -> Any: ...
