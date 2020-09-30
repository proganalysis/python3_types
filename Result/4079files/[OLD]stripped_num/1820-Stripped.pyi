# (generated with --quick)

from typing import Any
import unittest.case

Be: Any
BmcModel: Any
DumpType: Any
Node: Any
Polarity: Any
SatSolverFactory: Any
SatSolverResult: Any
StdioFile: Any
Wff: Any
bmc_exit: Any
deinit_nusmv: Any
go_bmc: Any
init_nusmv: Any
load_from_file: Any
ltlspec: Any
master_be_fsm: Any
parse_ltl_spec: Any
prop_database: Any
tests: Any
unittest: module
utils: Any

class TestBmcLTLSpec(unittest.case.TestCase):
    fsm: Any
    test_dump_dimacs_filename: Any
    def do_verify(self, problem) -> str: ...
    def test_bounded_semantics(self) -> None: ...
    def test_bounded_semantics_with_loop(self) -> None: ...
    def test_bounded_semantics_with_loop_optimized_depth1(self) -> None: ...
    def test_bounded_semantics_without_loop(self) -> None: ...
    def test_check_ltl(self) -> None: ...
    def test_check_ltl_incrementally(self) -> None: ...
    def test_dump_dimacs(self) -> None: ...
    def test_generate_ltl_problem(self) -> None: ...
