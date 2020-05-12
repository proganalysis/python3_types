# (generated with --quick)

from typing import Any

Instrument: Any
MockLC: Any
NP: Any
PhysContLPF: Any
SMContamination: Any
TabulatedFilter: Any
ceil: Any
inf: Any
sdss_g: Any
sdss_i: Any
sdss_r: Any
sdss_z: Any
sqrt: Any
subplots: Any
where: Any

class MockLPF(Any):
    _lc: Any
    b: Any
    cm: Any
    cteff: Any
    hteff: Any
    inc: Any
    instrument: Any
    k_apparent: Any
    know_host: Any
    misidentify_host: Any
    period: Any
    sma: Any
    t0_bjd: float
    def __init__(self, name: str, lc) -> None: ...
    def _init_instrument(self) -> None: ...
    def plot_light_curves(self, ncols: int = ..., figsize: tuple = ...) -> None: ...
    def posterior_samples(self, burn: int = ..., thin: int = ..., include_ldc: bool = ...) -> Any: ...
