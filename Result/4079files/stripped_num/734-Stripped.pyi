# (generated with --quick)

from typing import Any
import unittest.case

BDD: Any
BddFsm: Any
BddTrans: Any
PropDb: Any
car: Any
cdr: Any
deinit_nusmv: Any
evalSexp: Any
init_nusmv: Any
nsbddenc: Any
nsbddtrans: Any
nscompile: Any
nsenc: Any
nsfsm: Any
nsnode: Any
nsopt: Any
nsprop: Any
nsset: Any
nssexp: Any
nsutils: Any
unittest: module

class TestFlatHierarchy(unittest.case.TestCase):
    def model(self, filepath) -> Any: ...
    def print_mainFlatHierarchy(self, filepath) -> None: ...
    def test_admin(self) -> None: ...
    def test_constraints(self) -> None: ...
    def test_counters(self) -> None: ...
    def test_counters_assign(self) -> None: ...
    def test_mutex(self) -> None: ...
    def test_scheduler(self) -> None: ...
    def test_trans_flattening(self) -> None: ...
