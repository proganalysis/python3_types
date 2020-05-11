# (generated with --quick)

from typing import Any, NoReturn

dB2Linear: Any
np: module

class AntGainBS3GPP25996(AntGainBase):
    Am: float
    __doc__: str
    ant_gain: Any
    theta_3db: float
    def __init__(self, number_of_sectors = ...) -> None: ...
    def get_antenna_gain(self, angle) -> Any: ...

class AntGainBase(object):
    __doc__: str
    def get_antenna_gain(self, angle) -> NoReturn: ...

class AntGainOmni(AntGainBase):
    __doc__: str
    ant_gain: Any
    def __init__(self, ant_gain = ...) -> None: ...
    def get_antenna_gain(self, angle) -> Any: ...
