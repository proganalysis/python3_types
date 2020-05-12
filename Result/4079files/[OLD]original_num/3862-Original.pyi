# (generated with --quick)

from typing import Any
import unittest.case

Assembler: Any
ITERATIONS: int
MAX: int
MIN: int
Memory: Any
Processor: Any
op: Any
random: module
time: module
unittest: module

class AssemblerTest(unittest.case.TestCase):
    TIMEOUT: float
    a: Any
    proc: Any
    def test_runs(self) -> None: ...

class MemoryTests(unittest.case.TestCase):
    mem: Any
    def test_fetch_register(self) -> None: ...
    def test_register_edge(self) -> None: ...
    def test_set_fetch_register(self) -> None: ...
    def test_set_fetch_register_stress(self) -> None: ...

class OperationTests(unittest.case.TestCase):
    proc: Any
    r: Any
    def test_arithmetic_ops_stress(self) -> None: ...
    def test_arithmetic_ops_stress_const(self) -> None: ...
    def test_arithmetic_ops_stress_sum(self) -> None: ...
    def test_bitwise_ops(self) -> None: ...
    def test_bitwise_ops_stress(self) -> None: ...
    def test_call(self) -> None: ...

class ProcessorTests(unittest.case.TestCase):
    proc: Any
    def test_compare_jump(self) -> None: ...
    def test_data_ops(self) -> None: ...
    def test_performance(self) -> None: ...

def make_positive(a: int) -> int: ...
