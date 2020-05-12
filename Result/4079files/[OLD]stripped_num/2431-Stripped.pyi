# (generated with --quick)

import helpers.main_helper
import helpers.timer
import interfaces.LTL_to_automaton
import interfaces.LTS
import interfaces.func_description
import interfaces.solver_interface
import interfaces.spec
import synthesis.cobuchi_encoder
import synthesis.coreach_encoder
from typing import Any, Tuple, Type, TypeVar

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

_T1 = TypeVar('_T1')

def build_output_desc(output, is_moore, inputs) -> interfaces.func_description.FuncDesc: ...
def build_tau_desc(inputs) -> interfaces.func_description.FuncDesc: ...
def check_real(ltl_text, part_text, is_moore, ltl_to_atm, solver, max_k, min_size, max_size, opt_level = ...) -> Any: ...
def check_unreal(ltl_text, part_text, is_moore, ltl_to_atm, solver, max_k, min_size, max_size, opt_level = ...) -> Any: ...
def convert_tlsf_or_acacia_to_acacia(spec_file_name, is_moore_: _T1 = ...) -> Tuple[str, str, Any]: ...
def expr_size(e) -> Any: ...
def lts_to_dot(lts, state_variable, is_mealy) -> Any: ...
def main() -> Any: ...
def parse_acacia_and_build_expr(ltl_text, part_text, ltl_to_atm, strengthen_lvl) -> interfaces.spec.Spec: ...
def setup_logging(verbose_level = ..., filename = ..., name_processes = ...) -> logging.Logger: ...
