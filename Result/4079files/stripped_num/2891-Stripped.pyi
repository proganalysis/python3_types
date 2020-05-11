# (generated with --quick)

from typing import Any

Instrument: Any
ManualParameter: Any
VisaInstrument: Any
h5py: Any
logging: module
np: module
path: module
time: module
vals: Any

class Dummy_Duplexer(QuTech_Duplexer):
    _address: str
    _calibration_array: Any
    _dummy_instr: bool
    _terminator: str
    def __init__(self, name, nr_input_channels = ..., nr_output_channels = ..., **kw) -> None: ...
    def add_parameter(self, name, parameter_class = ..., **kwargs) -> None: ...

class QuTech_Duplexer(Any):
    SCPI_command_pause: float
    __doc__: str
    _calibration_array: Any
    _nr_input_channels: Any
    _nr_output_channels: Any
    def __init__(self, name, address = ..., reset = ..., nr_input_channels = ..., nr_output_channels = ...) -> None: ...
    def _mode_set_parser(self, val) -> str: ...
    def add_parameters(self, nr_input_channels, nr_output_channels) -> None: ...
    def calculate_attenuation(self, current_dac_value, scaling_factor) -> Any: ...
    def get_scaling_increment(self, scaling_factor) -> Any: ...
    def set_all_attenuations_to(self, val) -> None: ...
    def set_all_phases_to(self, val) -> None: ...
    def set_all_switches_to(self, mode) -> None: ...
