# (generated with --quick)

import __future__
from typing import Any

CoefficientData: Any
DigitalData: Any
PureData: Any
SolutionData: Any
division: __future__._Feature
np: module
print_function: __future__._Feature

class DigitalExample(Any):
    Tmax: float
    Tmin: float
    TminPsat: float
    description: str
    name: str
    reference: str
    xid: Any
    xmax: float
    xmin: float
    def __init__(self) -> None: ...

class DigitalExamplePure(Any, Any):
    Tmax: float
    Tmin: float
    TminPsat: float
    description: str
    name: str
    reference: str
    def __init__(self) -> None: ...

class MelinderExample(Any):
    Tbase: float
    Tmax: float
    Tmin: float
    TminPsat: float
    __doc__: str
    description: str
    name: str
    reference: str
    xbase: float
    xid: Any
    xmax: float
    xmin: float
    def __init__(self) -> None: ...

class PureExample(Any):
    Tmax: float
    Tmin: float
    TminPsat: float
    description: str
    name: str
    reference: str
    def __init__(self) -> None: ...

class SecCoolExample(Any):
    Tbase: float
    Tmax: float
    Tmin: float
    TminPsat: float
    __doc__: str
    description: str
    name: str
    xbase: float
    xid: Any
    xmax: float
    xmin: float
    def __init__(self) -> None: ...

class SolutionExample(Any):
    Tmax: Any
    Tmin: Any
    TminPsat: Any
    description: str
    name: str
    reference: str
    xid: Any
    xmax: Any
    xmin: Any
    def __init__(self) -> None: ...
