from typing import Any

def radiation_length(db: Any, material: Any): ...
def scattering_length(db: Any, material: Any): ...

class FermiRossi:
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs: Any) -> Any: ...

class DifferentialHighland:
    @staticmethod
    def l(x: Any, chi0: Any): ...
    @staticmethod
    def f_dh(l: Any): ...
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs: Any) -> Any: ...

class ICRU:
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs: Any) -> Any: ...

class ICRUProtons:
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs: Any) -> Any: ...

class DifferentialMoliere:
    @staticmethod
    def t(pv: float, p1v1: float, **kwargs: Any) -> Any: ...
    @staticmethod
    def f_dm(p1v1: float, pv: float) -> Any: ...
