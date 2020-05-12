from lyra.abstract_domains.container.fulara.key_wrapper import KeyWrapper
from lyra.abstract_domains.container.fulara.value_wrapper import ValueWrapper
from lyra.abstract_domains.numerical.interval_domain import IntervalState
from lyra.core.expressions import VariableIdentifier as VariableIdentifier
from typing import Any, Set

class IntervalSWrapper(IntervalState):
    def __init__(self, scalar_variables: Set[VariableIdentifier]) -> None: ...
    def add_variable(self, var: VariableIdentifier) -> Any: ...
    def remove_variable(self, var: VariableIdentifier) -> Any: ...
    def forget_variable(self, var: VariableIdentifier) -> Any: ...

class IntervalKWrapper(KeyWrapper, IntervalSWrapper):
    def __init__(self, scalar_variables: Set[VariableIdentifier], k_var: VariableIdentifier) -> None: ...
    def decomp(self, exclude: IntervalKWrapper) -> Set[IntervalKWrapper]: ...
    def is_singleton(self) -> bool: ...
    def __lt__(self, other: Any) -> Any: ...
    def __repr__(self): ...
    def is_bottom(self): ...

class IntervalVWrapper(ValueWrapper, IntervalSWrapper):
    def __init__(self, scalar_variables: Set[VariableIdentifier], v_var: VariableIdentifier) -> None: ...
    def __repr__(self): ...
    def is_bottom(self): ...
