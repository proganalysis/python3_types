# (generated with --quick)

from typing import Any, Dict, Optional, TypeVar

EnvironmentMixin: Any
IntervalLattice: Any
IntervalState: Any
KeyWrapper: Any
LengthIdentifier: Any
SequenceLyraType: Any
ValueWrapper: Any
VariableIdentifier: Any
copy_docstring: Any

_T = TypeVar('_T')

class IntervalKWrapper(Any, IntervalSWrapper):
    __doc__: str
    __lt__: Any
    decomp: Any
    is_bottom: Any
    is_singleton: Any
    def __init__(self, scalar_variables: set, k_var) -> None: ...
    def __repr__(self) -> str: ...

class IntervalSWrapper(Any):
    __doc__: str
    add_variable: Any
    remove_variable: Any
    def __init__(self, scalar_variables: set) -> None: ...
    def forget_variable(self, var) -> None: ...

class IntervalVWrapper(Any, IntervalSWrapper):
    __doc__: str
    is_bottom: Any
    def __init__(self, scalar_variables: set, v_var) -> None: ...
    def __repr__(self) -> str: ...

def copy(x: _T) -> _T: ...
def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
