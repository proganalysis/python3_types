from typing import Any

class WDFSA:
    _arcs: Any = ...
    _initial_states: Any = ...
    _final_states: Any = ...
    _vocabulary: Any = ...
    def __init__(self) -> None: ...
    def n_states(self): ...
    def n_arcs(self): ...
    def n_symbols(self): ...
    def _create_state(self, state: Any): ...
    def iterstates(self): ...
    def iterinitial(self): ...
    def iterfinal(self): ...
    def itersymbols(self): ...
    def iterarcs(self) -> None: ...
    def get_arcs(self, origin: Any, symbol: Any): ...
    def is_initial(self, state: Any): ...
    def is_final(self, state: Any): ...
    def add_arc(self, sfrom: Any, sto: Any, symbol: Any, weight: Any) -> None: ...
    def make_initial(self, state: Any) -> None: ...
    def make_final(self, state: Any) -> None: ...
    def path_weight(self, path: Any, semiring: Any): ...
    def arc_weight(self, origin: Any, destination: Any, sym: Any): ...
    def __str__(self): ...

def make_linear_fsa(sentence: Any, semiring: Any, terminal_constructor: Any = ...): ...
