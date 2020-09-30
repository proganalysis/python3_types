# (generated with --quick)

from typing import Any, TextIO, TypeVar

copy: module
istream: Any
itertools: module
mol: Any
mol_copy: Any
new_yaml_dict: Any
new_yaml_filename: str
np: module
oechem: Any
oeiupac: Any
os: module
pair: tuple
submit_eq: None
submit_neq: None
submiteqfile: TextIO
submitneqfile: TextIO
substituted_benzene_smilefile: str
substituted_benzenes_iupac: list
template_script_file_eq: str
template_script_file_neq: str
template_yamldict: Any
yaml: module
yaml_outfile: TextIO
yamlfile: TextIO

_T2 = TypeVar('_T2')

def create_submit_script(template_script_file, yaml_filename) -> None: ...
def create_yaml_file(mol_a, mol_b, yaml_dict: _T2) -> _T2: ...
