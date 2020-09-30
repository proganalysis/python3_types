# (generated with --quick)

from typing import Any, Callable, TypeVar

__author__: str
istravis: bool
os: module
run_oemol_test_suite: Callable
smiles_to_oemol: Any
test_OEMol_to_omm_ff: Callable
test_extractPositionsFromOEMol: Callable
test_get_data_filename: Callable
test_giveOpenmmPositionsToOEMol: Callable

_FT = TypeVar('_FT', bound=Callable)

def skipIf(condition: object, reason: str) -> Callable[[_FT], _FT]: ...
