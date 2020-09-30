# (generated with --quick)

from typing import Any

BaseLPF: Any
GParameter: Any
Instrument: Any
PParameter: Any
SMContamination: Any
UP: Any
arange: Any
as_from_rhop: Any
atleast_2d: Any
concatenate: Any
contaminate: Any
d_from_pkaiews: Any
i_from_ba: Any
i_from_baew: Any
inf: Any
isfinite: Any
map_ldc: Any
map_pv_pclpf: Any
njit: Any
prange: Any
repeat: Any
sdss_g: Any
sdss_i: Any
sdss_r: Any
sdss_z: Any
sqrt: Any
squeeze: Any
uniform: Any
where: Any
zeros: Any
zeros_like: Any

class ContaminatedLPF(Any):
    _pid_cn: Any
    _pid_k2: Any
    _sl_cn: Any
    _sl_k2: Any
    _start_k2: Any
    def _init_p_planet(self) -> None: ...
    def transit_model(self, pv) -> Any: ...

class PhysContLPF(Any):
    _pid_cn: Any
    _pid_k2: Any
    _sl_cn: Any
    _sl_k2: Any
    _start_k2: Any
    cm: Any
    instrument: Any
    def _init_instrument(self) -> None: ...
    def _init_p_planet(self) -> None: ...
    def additional_priors(self, pv) -> Any: ...
    def create_pv_population(self, npop = ...) -> Any: ...
    def posterior_samples(self, burn: int = ..., thin: int = ..., derived_parameters: bool = ...) -> Any: ...
    def transit_model(self, pvp) -> Any: ...
