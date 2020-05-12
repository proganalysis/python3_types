# (generated with --quick)

from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar

ResultFuture = `namedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`

ParameterClient: Any
ParameterGroup: Any
Result: Any
collections: module
dask: Any
dd: Any
lmfit: Any
matrix_calculation: Any
np: module
problem_bag: Any
residual_calculation: Any
residual_nnls: Any
residual_variable_projection: Any

_Tnamedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual = TypeVar('_Tnamedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual', bound=`namedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`)

class `namedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`(tuple):
    __slots__ = ["bag", "clp", "clp_label", "full_clp_label", "matrix", "residual"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str, str]
    bag: Any
    clp: Any
    clp_label: Any
    full_clp_label: Any
    matrix: Any
    residual: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`], bag, clp_label, matrix, full_clp_label, clp, residual) -> `_Tnamedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`: ...
    def _replace(self: `_Tnamedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`, **kwds) -> `_Tnamedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`: ...

def _create_result_data(parameter, scheme, result) -> Any: ...
def calculate_penalty(parameter, parameter_client, penalty_job) -> Any: ...
def create_problem(scheme, client, parameter_client) -> Tuple[Any, `namedtuple-ResultFuture-bag-clp_label-matrix-full_clp_label-clp-residual`]: ...
def optimize(scheme, verbose = ..., client = ...) -> Any: ...
def optimize_task(initial_parameter, scheme, verbose) -> Any: ...
