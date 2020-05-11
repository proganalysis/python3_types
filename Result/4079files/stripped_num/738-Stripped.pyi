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
    def t(pv, p1v1, **kwargs) -> Any: ...

class DifferentialMoliere:
    __doc__: str
    @staticmethod
    def f_dm(p1v1, pv) -> Any: ...
    @staticmethod
    def t(pv, p1v1, **kwargs) -> Any: ...

class FermiRossi:
    __doc__: str
    @staticmethod
    def t(pv, p1v1, **kwargs) -> Any: ...

class ICRU:
    __doc__: str
    @staticmethod
    def t(pv, p1v1, **kwargs) -> None: ...

class ICRUProtons:
    __doc__: str
    @staticmethod
    def t(pv, p1v1, **kwargs) -> Any: ...

def radiation_length(db, material) -> Any: ...
def scattering_length(db, material) -> Any: ...
