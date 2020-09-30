# (generated with --quick)

import openfisca_france_data
from typing import Any, Callable, Dict, Iterable, TypeVar

Famille: Any
Reform: Any
allocations_familiales_imposables: Any
cesthra_invalidee: Any
de_net_a_brut: Any
france_data_tax_benefit_system: openfisca_france_data.openfisca_france_data
inversion_directe_salaires: module
plf2015: Any
plf2016: Any
plf2016_ayrault_muet: Any
plfr2014: Any
reform_by_full_key: Dict[str, Any]
reform_list: Dict[str, Any]
scipy: Any
trannoy_wasmer: Any

_S = TypeVar('_S')
_T = TypeVar('_T')

def compose_reforms(reforms, tax_benefit_system) -> Any: ...
def get_cached_composed_reform(reform_keys, tax_benefit_system) -> Any: ...
def get_cached_reform(reform_key, tax_benefit_system) -> Any: ...
@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
