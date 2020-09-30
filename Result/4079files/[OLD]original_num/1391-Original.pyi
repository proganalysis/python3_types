# (generated with --quick)

from typing import Any
import unittest.case

CalculationRequest: Any
CalculationResponse: Any
Connector: Any
calculator_pb2: Any
grpc: Any
grpc_testing: Any
logging_pool: Any
target_service: Any
time: module
unittest: module

class CalculatorClientTest(unittest.case.TestCase):
    _client_execution_thread_pool: Any
    _fake_time: Any
    _fake_time_channel: Any
    _real_time: Any
    _real_time_channel: Any
    def test_successful_buffer3_sum(self) -> None: ...
    def test_successful_natural_numbers_lq(self) -> None: ...
    def test_successful_square(self) -> None: ...
    def test_successful_summation(self) -> None: ...
