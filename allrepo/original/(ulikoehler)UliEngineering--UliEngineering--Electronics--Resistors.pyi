# (generated with --quick)

import numpy
from typing import Any, List

Unit: Any
__all__: List[str]
e12: numpy.ndarray
e24: numpy.ndarray
e48: numpy.ndarray
e96: numpy.ndarray
itertools: module
normalize_numeric: Any
np: module

def current_through_resistor(resistor, voltage) -> Any: ...
def nearest_resistor(value, sequence = ...) -> Any: ...
def parallel_resistors(*args) -> Any: ...
def power_dissipated_in_resistor_by_current(resistor, current) -> Any: ...
def power_dissipated_in_resistor_by_voltage(resistor, voltage) -> Any: ...
def resistor_by_voltage_and_current(voltage, current) -> Any: ...
def resistor_range(multiplicator, sequence = ...) -> Any: ...
def serial_resistors(*args) -> Any: ...
def standard_resistors(minExp = ..., maxExp = ..., sequence = ...) -> itertools.chain[nothing]: ...
def voltage_across_resistor(resistor, current) -> Any: ...