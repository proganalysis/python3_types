# (generated with --quick)

from typing import Any

np: module
thickness: Any

class DifferentialHighland:
    __doc__: str
    @staticmethod
    def f_dh(l) -> Any: ...
    @staticmethod
    def l(x, chi0) -> Any: ...
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs) -> Any: ...

class DifferentialMoliere:
    __doc__: str
    @staticmethod
    def f_dm(p1v1: float, pv: float) -> Any: ...
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs) -> Any: ...

class FermiRossi:
    __doc__: str
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs) -> float: ...

class ICRU:
    __doc__: str
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs) -> None: ...

class ICRUProtons:
    __doc__: str
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs) -> Any: ...

def radiation_length(db, material) -> Any: ...
def scattering_length(db, material) -> Any: ...
