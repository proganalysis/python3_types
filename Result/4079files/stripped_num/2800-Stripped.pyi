# (generated with --quick)

import Error
import baseQubit
from typing import Any, Type

BaseQubit: Type[baseQubit.BaseQubit]
Bit: Type[Bit.Bit]
CodeError: Type[Error.CodeError]
EnvironmentError: Type[Error.EnvironmentError]
ExecuteModeError: Type[Error.ExecuteModeError]
GateNameError: Type[Error.GateNameError]
IBMError: Type[Error.IBMError]
IDRepeatError: Type[Error.IDRepeatError]
NoCloning: Type[Error.NoCloning]
NotNormal: Type[Error.NotNormal]
Qubit: Type[Qubit.Qubit]
Qubits: Type[Qubit.Qubits]
copy: module
get_curl_info: Any
interactCfg: Any
math: module
random: module
sys: module
writeErrorMsg: Any

class ControlFlow:
    ql: Any
    vl: Any
    def __enter__(self) -> bool: ...
    def __exit__(self, a, b, c) -> None: ...
    def __init__(self, q, v) -> None: ...

def __getattr__(name) -> Any: ...
def checkEnvironment() -> Any: ...
