# (generated with --quick)

from typing import Any, Iterable, Iterator, List, Tuple, TypeVar

ARG_A_STATE: Any
ARG_MODEL_STATE: Any
Automaton: Any
EncoderInterface: Any
FUNC_REACH: Any
FuncDesc: Any
LTS: Any
Signal: Any
TYPE_A_STATE: Any
TYPE_MODEL_STATE: Any
assertion: Any
bool_type: Any
call_func: Any
declare_const: Any
declare_enum: Any
declare_fun: Any
encode_get_model_values: Any
encode_model_bound: Any
encode_run_graph_ucw: Any
lmap: Any
log_entrance: Any
op_and: Any
op_implies: Any
op_not: Any
parse_model: Any
smt_name_m: Any
smt_name_q: Any

_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_T6 = TypeVar('_T6')

class CoreachEncoder(Any):
    automaton: Any
    descr_by_output: dict
    forbidding_atoms: List[str]
    inputs: list
    last_allowed_states: list
    max_k: Any
    max_model_states: list
    model_init_state: int
    parse_model: Any
    reach_func_desc: Any
    tau_desc: Any
    def __init__(self, automaton, tau_desc, inputs, descr_by_output, all_model_states, max_k, model_init_state = ...) -> None: ...
    def _declare_forbidding_atoms(self) -> Any: ...
    def _encode_automata_functions(self) -> list: ...
    def _encode_counters(self) -> list: ...
    def _encode_meaning_of_forbidding_atoms(self) -> list: ...
    def _encode_model_functions(self) -> list: ...
    def encode_assumption_forbid_k(self, k) -> list: ...
    def encode_get_model_values(self) -> Any: ...
    def encode_headers(self) -> list: ...
    def encode_initialization(self) -> list: ...
    def encode_model_bound(self, allowed_model_states) -> Any: ...
    def encode_run_graph(self, states_to_encode) -> Any: ...

@overload
def product(iter1: Iterable, iter2: Iterable, iter3: Iterable, iter4: Iterable, iter5: Iterable, iter6: Iterable, iter7: Iterable, *iterables: Iterable) -> Iterator[tuple]: ...
@overload
def product(iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4]) -> Iterator[Tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4], iter5: Iterable[_T5]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4], iter5: Iterable[_T5], iter6: Iterable[_T6]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
@overload
def product(*iterables: Iterable, repeat: int = ...) -> Iterator[tuple]: ...
