# (generated with --quick)

from typing import Any, Dict, List, Tuple

MSONable: Any
__author__: str
__copyright__: str
__date__: str
__email__: str
__maintainer__: str
__status__: str
__version__: str
itertools: module

class CovalentRadius:
    __doc__: str
    radius: Dict[str, float]
    def __init__(self) -> None: ...

class MoleculeStructureComparator(Any):
    __doc__: str
    bond_13_cap: Any
    bond_length_cap: Any
    covalent_radius: Any
    halogen_list: List[str]
    ignore_halogen_self_bond: bool
    ignore_ionic_bond: Any
    ionic_element_list: List[str]
    priority_bonds: Any
    priority_cap: Any
    def __init__(self, bond_length_cap = ..., covalent_radius = ..., priority_bonds = ..., priority_cap = ..., ignore_ionic_bond = ..., bond_13_cap = ...) -> None: ...
    def _get_bonds(self, mol) -> list: ...
    def are_equal(self, mol1, mol2) -> bool: ...
    def as_dict(self) -> Dict[str, Any]: ...
    @classmethod
    def from_dict(cls, d) -> MoleculeStructureComparator: ...
    @staticmethod
    def get_13_bonds(priority_bonds) -> Tuple[Tuple[nothing, ...], ...]: ...
