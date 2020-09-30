# (generated with --quick)

import mythril.analysis.symbolic
import mythril.laser.ethereum.cfg
import mythril.laser.ethereum.state.environment
import mythril.laser.ethereum.state.global_state
import mythril.laser.ethereum.taint_analysis
import mythril.laser.smt.expression
from typing import Type

Environment: Type[mythril.laser.ethereum.state.environment.Environment]
Expression: Type[mythril.laser.smt.expression.Expression]
GlobalState: Type[mythril.laser.ethereum.state.global_state.GlobalState]
JumpType: Type[mythril.laser.ethereum.cfg.JumpType]
Node: Type[mythril.laser.ethereum.cfg.Node]
SymExecWrapper: Type[mythril.analysis.symbolic.SymExecWrapper]
TaintRecord: Type[mythril.laser.ethereum.taint_analysis.TaintRecord]
TaintResult: Type[mythril.laser.ethereum.taint_analysis.TaintResult]
TaintRunner: Type[mythril.laser.ethereum.taint_analysis.TaintRunner]
copy: module
helper: module
log: logging.Logger
logging: module

def test_mutate_not_tainted() -> None: ...
def test_mutate_tainted() -> None: ...
