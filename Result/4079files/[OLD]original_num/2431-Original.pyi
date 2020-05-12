# (generated with --quick)

import helpers.main_helper
import helpers.timer
import interfaces.LTL_to_automaton
import interfaces.LTS
import interfaces.expr
import interfaces.func_description
import interfaces.solver_interface
import interfaces.spec
import synthesis.cobuchi_encoder
import synthesis.coreach_encoder
from typing import Any, Iterable, Optional, Tuple, Type, TypeVar

ARG_MODEL_STATE: str
CoBuchiEncoder: Type[synthesis.cobuchi_encoder.CoBuchiEncoder]
CoreachEncoder: Type[synthesis.coreach_encoder.CoreachEncoder]
LTLToAutomaton: Type[interfaces.LTL_to_automaton.LTLToAutomaton]
LTS: Type[interfaces.LTS.LTS]
REALIZABLE_RC: int
SolverInterface: Type[interfaces.solver_interface.SolverInterface]
Timer: Type[helpers.timer.Timer]
UNKNOWN_RC: int
UNREALIZABLE_RC: int
Z3SolverFactory: Type[helpers.main_helper.Z3SolverFactory]
Z3_PATH: Any
argparse: module
automaton_to_dot: module
k_reduce: Any
logging: module
model_k_searcher: module
model_searcher: module
tempfile: module
translator_via_ltl3ba: module
translator_via_spot: module

_T0 = TypeVar('_T0')

def build_output_desc(output: interfaces.expr.Signal, is_moore, inputs: Iterable[interfaces.expr.Signal]) -> interfaces.func_description.FuncDesc: ...
def build_tau_desc(inputs: Iterable[interfaces.expr.Signal]) -> interfaces.func_description.FuncDesc: ...
def check_real(ltl_text, part_text, is_moore, ltl_to_atm: interfaces.LTL_to_automaton.LTLToAutomaton, solver: interfaces.solver_interface.SolverInterface, max_k: int, min_size, max_size, opt_level = ...) -> interfaces.LTS.LTS: ...
def check_unreal(ltl_text, part_text, is_moore, ltl_to_atm: interfaces.LTL_to_automaton.LTLToAutomaton, solver: interfaces.solver_interface.SolverInterface, max_k: int, min_size, max_size, opt_level = ...) -> interfaces.LTS.LTS: ...
def convert_tlsf_or_acacia_to_acacia(spec_file_name: str, is_moore_: _T0 = ...) -> Tuple[str, str, Any]: ...
def expr_size(e: interfaces.expr.Expr) -> int: ...
def lts_to_dot(lts: interfaces.LTS.LTS, state_variable, is_mealy) -> str: ...
def main() -> Any: ...
def parse_acacia_and_build_expr(ltl_text: str, part_text: str, ltl_to_atm: interfaces.LTL_to_automaton.LTLToAutomaton, strengthen_lvl) -> interfaces.spec.Spec: ...
def setup_logging(verbose_level: int = ..., filename: Optional[str] = ..., name_processes: bool = ...) -> logging.Logger: ...
